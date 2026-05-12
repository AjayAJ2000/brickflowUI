import React, { useState, useEffect, useCallback, useRef } from 'react'
import { Renderer } from './Renderer'
import type { VNodeData, ServerMessage, Patch } from './types'

type WsStatus = 'connecting' | 'connected' | 'disconnected' | 'error'

type LoadingBootstrap = {
  title?: string
  message?: string
  subtitle?: string
  reconnectingMessage?: string
  errorMessage?: string
  animation?: string
  textOnly?: boolean
  asset?: string | null
  assetKind?: 'image' | 'video' | null
  video?: string | null
  themeMode?: 'light' | 'dark'
}

declare global {
  interface Window {
    __BRICKFLOW_BOOTSTRAP__?: LoadingBootstrap
  }
}

const LOADING_BOOTSTRAP: LoadingBootstrap = window.__BRICKFLOW_BOOTSTRAP__ || {}

function applyPatch(tree: VNodeData, patch: Patch): VNodeData {
  const { op, path, node, props } = patch

  if (path.length === 0) {
    if (op === 'replace' && node) return node
    if (op === 'update_props' && props) {
      const nextProps = { ...tree.props }
      for (const [key, value] of Object.entries(props)) {
        if (value === null) delete nextProps[key]
        else nextProps[key] = value
      }
      return { ...tree, props: nextProps }
    }
    return tree
  }

  const [idx, ...rest] = path
  const newChildren = [...tree.children]

  if (op === 'remove' && rest.length === 0) {
    newChildren.splice(idx, 1)
    return { ...tree, children: newChildren }
  }

  if (op === 'insert' && rest.length === 0 && node) {
    newChildren.splice(idx, 0, node)
    return { ...tree, children: newChildren }
  }

  if (idx < newChildren.length) {
    newChildren[idx] = applyPatch(newChildren[idx], { op, path: rest, node, props })
  } else if (op === 'insert' && node) {
    newChildren.push(node)
  }

  return { ...tree, children: newChildren }
}

function LoadingVisual({ status }: { status: WsStatus }) {
  const asset = LOADING_BOOTSTRAP.video || LOADING_BOOTSTRAP.asset
  const kind = LOADING_BOOTSTRAP.video ? 'video' : LOADING_BOOTSTRAP.assetKind
  const animation = LOADING_BOOTSTRAP.animation || 'spinner'
  const title = LOADING_BOOTSTRAP.title || 'BrickflowUI'
  const subtitle = LOADING_BOOTSTRAP.subtitle
  const message =
    status === 'connecting'
      ? (LOADING_BOOTSTRAP.message || 'Connecting to runtime...')
      : status === 'disconnected'
        ? (LOADING_BOOTSTRAP.reconnectingMessage || 'Reconnecting...')
        : status === 'error'
          ? (LOADING_BOOTSTRAP.errorMessage || 'Connection error - retrying...')
          : 'Loading...'

  return (
    <div className={`bf-loading-screen bf-loading-${animation}`}>
      {!LOADING_BOOTSTRAP.textOnly ? (
        kind === 'video' && asset ? (
          <video
            className="bf-loading-media"
            src={asset}
            autoPlay
            muted
            loop
            playsInline
          />
        ) : asset ? (
          <img className="bf-loading-media" src={asset} alt={`${title} loading`} />
        ) : (
          <div className={`bf-spinner bf-spinner-lg ${animation === 'pulse' ? 'bf-spinner-pulse' : ''}`} />
        )
      ) : null}
      <div className="bf-loading-brand">{title}</div>
      {subtitle ? <div className="bf-loading-subtitle">{subtitle}</div> : null}
      <div className="bf-loading-hint">{message}</div>
    </div>
  )
}

function resolveInitialThemeMode(): 'light' | 'dark' {
  const bootstrapMode = LOADING_BOOTSTRAP.themeMode === 'light' ? 'light' : 'dark'
  try {
    const stored = window.localStorage.getItem('brickflowui.theme')
    return stored === 'light' || stored === 'dark' ? stored : bootstrapMode
  } catch {
    return bootstrapMode
  }
}

export default function App() {
  const [vdom, setVdom] = useState<VNodeData | null>(null)
  const [status, setStatus] = useState<WsStatus>('connecting')
  const [error, setError] = useState<string | null>(null)
  const [pendingEvents, setPendingEvents] = useState<Set<string>>(new Set())
  const [themeMode, setThemeModeState] = useState<'light' | 'dark'>(resolveInitialThemeMode)
  const wsRef = useRef<WebSocket | null>(null)
  const vdomRef = useRef<VNodeData | null>(null)

  const dispatch = useCallback((event_id: string, data: Record<string, unknown> = {}) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      setPendingEvents((prev) => {
        const next = new Set(prev)
        next.add(event_id)
        return next
      })
      wsRef.current.send(JSON.stringify({ type: 'event', event_id, data }))
    }
  }, [])

  const setThemeMode = useCallback((mode: 'light' | 'dark') => {
    setThemeModeState(mode)
    document.documentElement.dataset.themeMode = mode
    try {
      window.localStorage.setItem('brickflowui.theme', mode)
    } catch {
      // Ignore storage issues in locked-down runtimes.
    }
  }, [])

  const navigate = useCallback((path: string) => {
    if (wsRef.current?.readyState === WebSocket.OPEN) {
      wsRef.current.send(JSON.stringify({ type: 'navigate', path }))
      window.history.pushState({}, '', path)
    }
  }, [])

  useEffect(() => {
    document.documentElement.dataset.themeMode = themeMode
  }, [themeMode])

  useEffect(() => {
    let reconnectTimer: ReturnType<typeof setTimeout>

    function connect() {
      const proto = location.protocol === 'https:' ? 'wss' : 'ws'
      const ws = new WebSocket(`${proto}://${location.host}/events?path=${encodeURIComponent(window.location.pathname)}`)
      wsRef.current = ws
      setStatus('connecting')

      ws.onopen = () => {
        setStatus('connected')
        setError(null)
      }

      ws.onmessage = (e: MessageEvent) => {
        try {
          const msg: ServerMessage = JSON.parse(e.data as string)

          if (msg.type === 'full') {
            vdomRef.current = msg.tree
            setVdom(msg.tree)
          } else if (msg.type === 'patch') {
            if (vdomRef.current) {
              let updated = vdomRef.current
              for (const patch of msg.patches) {
                updated = applyPatch(updated, patch)
              }
              vdomRef.current = updated
              setVdom({ ...updated })
            }
          } else if (msg.type === 'event_complete') {
            setPendingEvents((prev) => {
              if (!prev.has(msg.event_id)) return prev
              const next = new Set(prev)
              next.delete(msg.event_id)
              return next
            })
          } else if (msg.type === 'error') {
            setError(msg.message)
          }
        } catch (err) {
          console.error('[BrickflowUI] Failed to parse server message', err)
        }
      }

      ws.onclose = () => {
        setStatus('disconnected')
        setPendingEvents(new Set())
        reconnectTimer = setTimeout(connect, 2500)
      }

      ws.onerror = () => {
        setStatus('error')
        setPendingEvents(new Set())
        ws.close()
      }
    }

    connect()

    const handlePopstate = () => navigate(window.location.pathname)
    window.addEventListener('popstate', handlePopstate)

    return () => {
      clearTimeout(reconnectTimer)
      wsRef.current?.close()
      window.removeEventListener('popstate', handlePopstate)
    }
  }, [navigate])

  if (!vdom) {
    return <LoadingVisual status={status} />
  }

  return (
    <>
      <div className="bf-page-shell">
        <Renderer
          node={vdom}
          dispatch={dispatch}
          navigate={navigate}
          pendingEvents={pendingEvents}
          themeMode={themeMode}
          setThemeMode={setThemeMode}
        />
      </div>
      {status === 'disconnected' && (
        <div className="bf-connection-banner">Reconnecting to server...</div>
      )}
      {error && (
        <div className="bf-connection-banner" style={{ borderColor: 'var(--db-error)', color: 'var(--db-error)', background: 'var(--db-error-bg)' }}>
          Runtime error: {error}
        </div>
      )}
    </>
  )
}
