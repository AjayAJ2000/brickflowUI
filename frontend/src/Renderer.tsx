import React, { useEffect, useState } from 'react'
import type { VNodeData } from './types'
import {
  AreaChart, Area,
  BarChart, Bar,
  LineChart, Line,
  PieChart, Pie, Cell,
  XAxis, YAxis, CartesianGrid, Tooltip, Legend,
  ResponsiveContainer
} from 'recharts'

// ── Lucide icon lookup ────────────────────────────────────────────────────
// We only load icons used by the navigation system; others render as text
const LUCIDE_ICON_MAP: Record<string, string> = {
  Home: 'M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z M9 22V12h6v10',
  Database: 'M12 2C6.48 2 2 4.24 2 7s4.48 5 10 5 10-2.24 10-5S17.52 2 12 2zM2 17c0 2.76 4.48 5 10 5s10-2.24 10-5M2 12c0 2.76 4.48 5 10 5s10-2.24 10-5',
  LayoutDashboard: 'M3 3h7v7H3zM14 3h7v7h-7zM14 14h7v7h-7zM3 14h7v7H3z',
  GitBranch: 'M6 3v12M18 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM6 21a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM18 9a9 9 0 0 1-9 9',
  FlaskConical: 'M14 2v6l3 10H7L10 8V2M8.5 2h7',
  Settings: 'M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1-2.83 2.83l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83-2.83l.06-.06A1.65 1.65 0 0 0 4.68 15a1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 2.83-2.83l.06.06A1.65 1.65 0 0 0 9 4.68a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 2.83l-.06.06A1.65 1.65 0 0 0 19.4 9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z',
  Lock: 'M19 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2zM7 11V7a5 5 0 0 1 10 0v4',
  Hash: 'M4 9h16M4 15h16M10 3L8 21M16 3l-2 18',
  Activity: 'M22 12h-4l-3 9L9 3l-3 9H2',
  Clock: 'M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM12 6v6l4 2',
  Server: 'M2 3h20v6H2zM2 15h20v6H2zM6 9v6M18 9v6',
  AlertTriangle: 'M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0zM12 9v4M12 17h.01',
  CheckCircle: 'M22 11.08V12a10 10 0 1 1-5.93-9.14M22 4L12 14.01l-3-3',
  XCircle: 'M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM15 9l-6 6M9 9l6 6',
  PlayCircle: 'M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM10 8l6 4-6 4V8z',
  Target: 'M12 22c5.523 0 10-4.477 10-10S17.523 2 12 2 2 6.477 2 12s4.477 10 10 10zM12 18a6 6 0 1 0 0-12 6 6 0 0 0 0 12zM12 14a2 2 0 1 0 0-4 2 2 0 0 0 0 4zM22 12h-2M2 12h2M12 2v2M12 22v-2',
  Sparkles: 'M12 3l1.8 4.2L18 9l-4.2 1.8L12 15l-1.8-4.2L6 9l4.2-1.8L12 3zM19 15l.9 2.1L22 18l-2.1.9L19 21l-.9-2.1L16 18l2.1-.9L19 15zM5 15l.9 2.1L8 18l-2.1.9L5 21l-.9-2.1L2 18l2.1-.9L5 15z',
  Inbox: 'M4 4h16v10l-3 4H7l-3-4V4zM4 14h4l2 3h4l2-3h4',
  X: 'M18 6L6 18M6 6l12 12',
}

const CHART_COLORS = ['#FF3621', '#58a6ff', '#3fb950', '#e3b341', '#bc8cff', '#d28c3c']

// ── Render context ─────────────────────────────────────────────────────────
interface RenderCtx {
  dispatch: (event_id: string, data?: Record<string, unknown>) => void
  navigate: (path: string) => void
}

// ── Icon component ──────────────────────────────────────────────────────────
function Icon({ name, size = 16 }: { name: string; size?: number }) {
  const path = LUCIDE_ICON_MAP[name]
  if (!path) return <span style={{ fontSize: size - 2, opacity: 0.6 }}>◆</span>
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width={size}
      height={size}
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      {path.split('M').filter(Boolean).map((d, i) => (
        <path key={i} d={'M' + d} />
      ))}
    </svg>
  )
}

function resolveMotionClass(props: Record<string, any>, base: string[] = []) {
  const classes = [...base]
  if (props.animated) classes.push('bf-animated')
  if (props.elevated) classes.push('bf-elevated')
  if (props.loading) classes.push('bf-is-loading')
  if (props.animation) classes.push(`bf-anim-${props.animation}`)
  return classes.filter(Boolean).join(' ')
}

function resolveMotionStyle(props: Record<string, any>) {
  const style = { ...(props.style as object || {}) } as React.CSSProperties
  if (props.animationDelay !== undefined && props.animationDelay !== null) {
    style.animationDelay = `${props.animationDelay}s`
  }
  return style
}

function renderLoadingSkeleton(lines = 3) {
  return (
    <div className="bf-skeleton-stack">
      {Array.from({ length: lines }).map((_, index) => (
        <div key={index} className="bf-skeleton-line" />
      ))}
    </div>
  )
}

// ── Main recursive renderer ────────────────────────────────────────────────
export function Renderer({ node, dispatch, navigate }: { node: VNodeData; dispatch: RenderCtx['dispatch']; navigate: RenderCtx['navigate'] }) {
  const ctx: RenderCtx = { dispatch, navigate }
  return <>{renderNode(node, ctx, '0')}</>
}

function renderChildren(children: VNodeData[], ctx: RenderCtx, prefix: string) {
  return children.map((child, i) => renderNode(child, ctx, `${prefix}-${i}`))
}

function renderNode(node: VNodeData, ctx: RenderCtx, key: string): React.ReactNode {
  if (!node) return null
  const { type, props, children } = node
  const p = props as Record<string, any>

  const ev = (eventName: string, arg?: unknown) => {
    const eventId = p[eventName] as string | undefined
    if (eventId) ctx.dispatch(eventId, arg ? { value: arg } : {})
  }

  switch (type) {

    // ── Text ───────────────────────────────────────────────────────────────
    case 'Text': {
      const variant = (p.variant as string) || 'body'
      const cls = ['bf-text-' + variant, p.muted ? 'bf-text-muted' : '', p.bold ? 'bf-text-bold' : '', p.italic ? 'bf-text-italic' : ''].filter(Boolean).join(' ')
      const Tag = ({ h1: 'h1', h2: 'h2', h3: 'h3', h4: 'h4', code: 'code', label: 'label', caption: 'small' } as Record<string, string>)[variant] || 'p'
      return React.createElement(Tag, { key, className: cls, style: p.color ? { color: p.color as string } : undefined }, p.value as string)
    }

    case 'Code':
      return <pre key={key} className="bf-code-block"><code>{p.value as string}</code></pre>

    // ── Layout ─────────────────────────────────────────────────────────────
    case 'Column': {
      const pad = ((p.padding as number) || 0) * 4
      const gap = ((p.gap as number) || 2) * 4
      const alignMap: Record<string, string> = { start: 'flex-start', end: 'flex-end', center: 'center', stretch: 'stretch' }
      return (
        <div key={key} className="bf-column" style={{ display: 'flex', flexDirection: 'column', gap, padding: pad, alignItems: alignMap[p.align as string] || 'stretch', width: '100%', ...(p.style as object || {}) }}>
          {renderChildren(children, ctx, key)}
        </div>
      )
    }

    case 'Row': {
      const gap = ((p.gap as number) || 2) * 4
      const alignMap: Record<string, string> = { start: 'flex-start', end: 'flex-end', center: 'center', stretch: 'stretch' }
      const justifyMap: Record<string, string> = { start: 'flex-start', end: 'flex-end', center: 'center', between: 'space-between', around: 'space-around' }
      return (
        <div key={key} className="bf-row" style={{ display: 'flex', flexDirection: 'row', gap, flexWrap: p.wrap !== false ? 'wrap' : 'nowrap', alignItems: alignMap[p.align as string] || 'center', justifyContent: justifyMap[p.justify as string] || 'flex-start', width: '100%', ...(p.style as object || {}) }}>
          {renderChildren(children, ctx, key)}
        </div>
      )
    }

    case 'Card': {
      const cls = resolveMotionClass(p, ['bf-card', p.bordered ? 'bordered' : '', p.hover ? 'hoverable' : ''])
      const pad = ((p.padding as number) || 5) * 4
      return (
        <div key={key} className={cls} style={{ padding: pad, ...resolveMotionStyle(p) }}>
          {(p.title || p.subtitle) ? (
            <div className="bf-card-header">
              {p.title ? <div className="bf-card-title">{p.title as string}</div> : null}
              {p.subtitle ? <div className="bf-card-subtitle">{p.subtitle as string}</div> : null}
            </div>
          ) : null}
          {renderChildren(children, ctx, key)}
        </div>
      )
    }

    case 'Grid': {
      const cols = (p.cols as number) || 2
      const gap = ((p.gap as number) || 4) * 4
      return (
        <div key={key} className="bf-grid" style={{ '--cols': cols, gap } as React.CSSProperties}>
          {renderChildren(children, ctx, key)}
        </div>
      )
    }

    case 'Divider':
      return p.label
        ? <div key={key} className="bf-divider-labeled"><span>{p.label as string}</span></div>
        : <hr key={key} className="bf-divider" />

    case 'Spacer':
      return <div key={key} style={{ height: ((p.size as number) || 4) * 4 }} />

    // ── Controls ───────────────────────────────────────────────────────────
    case 'Button':
      return (
        <button
          key={key}
          className={resolveMotionClass(p, ['bf-btn', `bf-btn-${(p.variant as string) || 'primary'}`])}
          disabled={(p.disabled as boolean) || (p.loading as boolean) || false}
          type={(p.htmlType as 'button' | 'submit' | 'reset') || 'button'}
          style={resolveMotionStyle(p)}
          onClick={() => ev('click')}
        >
          {p.loading && <span className="bf-spinner bf-spinner-sm" />}
          {p.icon && <Icon name={p.icon as string} size={14} />}
          {p.label as string}
        </button>
      )

    case 'Input':
      return (
        <div key={key} className={resolveMotionClass(p, ['bf-form-field'])} style={resolveMotionStyle(p)}>
          {p.label && <label className="bf-label">{p.label as string}</label>}
          {p.loading && <div className="bf-field-loading"><div className="bf-spinner bf-spinner-sm" /></div>}
          {p.inputType === 'textarea'
            ? <textarea
                name={p.name as string}
                className="bf-textarea"
                placeholder={p.placeholder as string}
                value={(p.value as string) || ''}
                disabled={p.disabled as boolean}
                onChange={e => ev('change', e.target.value)}
              />
            : <input
                name={p.name as string}
                className={`bf-input${p.error ? ' error' : ''}`}
                type={(p.inputType as string) || 'text'}
                placeholder={(p.placeholder as string) || ''}
                value={(p.value as string) || ''}
                disabled={p.disabled as boolean}
                onChange={e => ev('change', e.target.value)}
              />
          }
          {p.error && <span className="bf-input-error">{p.error as string}</span>}
        </div>
      )

    case 'DateRangePicker':
      return <DateRangePickerComponent key={key} props={p} dispatch={(value) => ev('change', value)} />

    case 'MultiSelect':
      return <MultiSelectComponent key={key} props={p} dispatch={(value) => ev('change', value)} />

    case 'Select':
      return (
        <div key={key} className={resolveMotionClass(p, ['bf-form-field'])} style={resolveMotionStyle(p)}>
          {p.label && <label className="bf-label">{p.label as string}</label>}
          {p.loading && <div className="bf-field-loading"><div className="bf-spinner bf-spinner-sm" /></div>}
          <select
            name={p.name as string}
            className="bf-select"
            value={(p.value as string) || ''}
            disabled={p.disabled as boolean}
            onChange={e => ev('change', e.target.value)}
          >
            {p.placeholder && <option value="">{p.placeholder as string}</option>}
            {((p.options as Array<{ label: string; value: string }>) || []).map(opt => (
              <option key={opt.value} value={opt.value}>{opt.label}</option>
            ))}
          </select>
        </div>
      )

    case 'Checkbox':
      return (
        <label key={key} className="bf-checkbox-wrapper">
          <input
            type="checkbox"
            name={p.name as string}
            checked={Boolean(p.checked)}
            disabled={p.disabled as boolean}
            onChange={e => ev('change', e.target.checked)}
          />
          {p.label as string}
        </label>
      )

    case 'Toggle': {
      return (
        <ToggleComponent key={key} props={p} dispatch={(v) => ev('change', v)} />
      )
    }

    case 'Slider':
      return (
        <div key={key} className="bf-slider-wrapper">
          {p.label && <label className="bf-label">{p.label as string}</label>}
          <input
            type="range"
            className="bf-slider"
            name={p.name as string}
            min={p.min as number}
            max={p.max as number}
            step={p.step as number}
            value={p.value as number}
            onChange={e => ev('change', parseFloat(e.target.value))}
          />
        </div>
      )

    // ── Data display ───────────────────────────────────────────────────────
    case 'Breadcrumbs':
      return (
        <nav key={key} className="bf-breadcrumbs" aria-label="Breadcrumb">
          {((p.items as Array<Record<string, any>>) || []).map((item, index, items) => {
            const isLast = index === items.length - 1
            return (
              <React.Fragment key={`${key}-crumb-${index}`}>
                {isLast || !item.path ? (
                  <span className="bf-breadcrumb-current">{String(item.label ?? '')}</span>
                ) : (
                  <button type="button" className="bf-breadcrumb-link" onClick={() => ctx.navigate(String(item.path))}>
                    {String(item.label ?? '')}
                  </button>
                )}
                {!isLast ? <span className="bf-breadcrumb-sep">/</span> : null}
              </React.Fragment>
            )
          })}
        </nav>
      )

    case 'EmptyState':
      return (
        <div key={key} className="bf-empty-state">
          <div className="bf-empty-state-icon">
            <Icon name={(p.icon as string) || 'Inbox'} size={18} />
          </div>
          <div className="bf-empty-state-title">{p.title as string}</div>
          <div className="bf-empty-state-message">{p.message as string}</div>
          {(p.actions as VNodeData[] | undefined)?.length ? (
            <div className="bf-empty-state-actions">
              {renderChildren((p.actions as VNodeData[]) || [], ctx, `${key}-actions`)}
            </div>
          ) : null}
        </div>
      )

    case 'Table':
      return <TableComponent key={key} props={p} dispatch={ctx.dispatch} />

    case 'Badge':
      return <span key={key} className={`bf-badge bf-badge-${(p.color as string) || 'blue'}`}>{p.label as string}</span>

    case 'Alert':
      return (
        <div key={key} className={`bf-alert bf-alert-${(p.alertType as string) || 'info'}`}>
          {p.title && <div className="bf-alert-title">{p.title as string}</div>}
          {p.message as string}
        </div>
      )

    case 'Spinner':
      return <div key={key} className={`bf-spinner bf-spinner-${(p.size as string) || 'md'}`} />

    case 'Progress': {
      const pct = Math.min(100, (((p.value as number) / (p.max as number || 100)) * 100))
      return (
        <div key={key} className={resolveMotionClass(p, ['bf-progress-wrapper'])} style={resolveMotionStyle(p)}>
          {p.label && <div className="bf-progress-label"><span>{p.label as string}</span><span>{Math.round(pct)}%</span></div>}
          <div className="bf-progress-track">
            <div className={`bf-progress-fill ${p.animated ? 'animated' : ''}`} style={{ width: `${pct}%`, background: `var(--db-${p.color || 'primary'})` }} />
          </div>
        </div>
      )
    }

    case 'Stat': {
      const deltaType = (p.deltaType as string) || 'neutral'
      return (
        <div key={key} className={resolveMotionClass(p, ['bf-stat'])} style={resolveMotionStyle(p)}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            {p.icon && <Icon name={p.icon as string} size={16} />}
            <div className="bf-stat-label">{p.label as string}</div>
          </div>
          <AnimatedValue value={p.value as string} animated={Boolean(p.animated)} />
          {p.delta && <div className={`bf-stat-delta ${deltaType}`}>{deltaType === 'increase' ? '▲' : deltaType === 'decrease' ? '▼' : '—'} {p.delta as string}</div>}
        </div>
      )
    }

    // ── Navigation ──────────────────────────────────────────────────────────
    case 'Sidebar': {
      const activePath = window.location.pathname
      return (
        <aside key={key} className="bf-sidebar">
          <div className="bf-sidebar-brand">
            {p.logo
              ? <img src={p.logo as string} alt="logo" width={28} height={28} style={{ borderRadius: 6 }} />
              : <div className="bf-sidebar-brand-logo">{((p.brandName as string) || 'B').charAt(0)}</div>
            }
            <span className="bf-sidebar-brand-name">{p.brandName as string}</span>
          </div>
          <nav className="bf-nav-section">
            {children.map((child, i) => {
              const cp = child.props as Record<string, any>
              const isActive = activePath === (cp.path as string)
              return (
                <button
                  key={i}
                  className={`bf-nav-item ${isActive ? 'active' : ''}`}
                  onClick={() => ctx.navigate(cp.path as string)}
                >
                  {cp.icon && <span className="bf-nav-icon"><Icon name={cp.icon as string} size={16} /></span>}
                  {cp.label as string}
                  {cp.badge && <span className="bf-nav-badge">{cp.badge as string}</span>}
                </button>
              )
            })}
          </nav>
        </aside>
      )
    }

    // NavItem is rendered as part of Sidebar above; standalone fallback:
    case 'NavItem':
      return (
        <button key={key} className="bf-nav-item" onClick={() => ctx.navigate(p.path as string)}>
          {p.icon && <Icon name={p.icon as string} size={16} />}
          {p.label as string}
        </button>
      )

    // ── Tabs ───────────────────────────────────────────────────────────────
    case 'Tabs':
      return <TabsComponent key={key} props={p} children={children} ctx={ctx} nodeKey={key} dispatch={ctx.dispatch} />

    case 'TabItem':
      return null // Rendered inside Tabs

    // ── Modal ──────────────────────────────────────────────────────────────
    case 'Accordion':
      return <AccordionComponent key={key} props={p} children={children} ctx={ctx} nodeKey={key} />

    case 'AccordionItem':
      return null

    case 'Modal':
      if (!p.visible) return null
      return (
        <div key={key} className="bf-modal-overlay" onClick={() => ev('close')}>
          <div className={`bf-modal bf-modal-${(p.size as string) || 'md'}`} onClick={e => e.stopPropagation()}>
            <div className="bf-modal-header">
              <span className="bf-modal-title">{p.title as string}</span>
              <button className="bf-modal-close" onClick={() => ev('close')}><Icon name="X" size={16} /></button>
            </div>
            <div className="bf-modal-body">{renderChildren(children, ctx, key)}</div>
          </div>
        </div>
      )

    // ── Form ───────────────────────────────────────────────────────────────
    case 'Drawer':
      if (!p.visible) return null
      return (
        <div key={key} className="bf-drawer-overlay" onClick={() => ev('close')}>
          <div className={`bf-drawer bf-drawer-${(p.side as string) || 'right'}`} style={{ width: (p.width as string) || '420px' }} onClick={e => e.stopPropagation()}>
            <div className="bf-drawer-header">
              <span className="bf-drawer-title">{p.title as string}</span>
              <button className="bf-modal-close" onClick={() => ev('close')}><Icon name="X" size={16} /></button>
            </div>
            <div className="bf-drawer-body">{renderChildren(children, ctx, key)}</div>
          </div>
        </div>
      )

    case 'Form':
      return (
        <form
          key={key}
          className="bf-form"
          onSubmit={async (e) => {
            e.preventDefault()
            const data: Record<string, unknown> = {}
            new FormData(e.currentTarget).forEach((v, k) => {
              if (k in data) {
                const current = data[k]
                if (Array.isArray(current)) current.push(v)
                else data[k] = [current, v]
              } else {
                data[k] = v
              }
            })
            const resp = await fetch(p.action as string, {
              method: (p.method as string) || 'POST',
              credentials: 'same-origin',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify(data),
            })
            if (resp.ok && p.successRedirect) {
              if (p.reloadOnSuccess) {
                window.location.assign(p.successRedirect as string)
              } else {
                ctx.navigate(p.successRedirect as string)
              }
            }
          }}
        >
          {renderChildren(children, ctx, key)}
        </form>
      )

    // ── Charts ─────────────────────────────────────────────────────────────
    case 'AreaChart': {
      const yKeys = (p.yKeys as string[]) || []
      const data = (p.data as object[]) || []
      if (p.loading) return <div key={key} className="bf-chart-state">{renderLoadingSkeleton(4)}</div>
      if (!data.length) return <div key={key} className="bf-chart-state">{(p.emptyMessage as string) || 'No chart data available'}</div>
      return (
        <div key={key} className="bf-chart-container">
          {p.title && <div className="bf-chart-title">{p.title as string}</div>}
          <ResponsiveContainer width="100%" height={(p.height as number) || 300}>
            <AreaChart data={data} onClick={(state) => p.click && ev('click', state?.activePayload?.[0]?.payload ?? {})}>
              <defs>
                {yKeys.map((yk, i) => (
                  <linearGradient key={yk} id={`agrad-${i}`} x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor={(p.colors as string[])?.[i] || CHART_COLORS[i % CHART_COLORS.length]} stopOpacity={0.25} />
                    <stop offset="95%" stopColor={(p.colors as string[])?.[i] || CHART_COLORS[i % CHART_COLORS.length]} stopOpacity={0} />
                  </linearGradient>
                ))}
              </defs>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={p.xKey as string} />
              <YAxis />
              <Tooltip />
              {yKeys.map((yk, i) => (
                <Area key={yk} type="monotone" dataKey={yk} stroke={(p.colors as string[])?.[i] || CHART_COLORS[i % CHART_COLORS.length]} fill={`url(#agrad-${i})`} strokeWidth={2} />
              ))}
            </AreaChart>
          </ResponsiveContainer>
        </div>
      )
    }

    case 'LineChart': {
      const yKeys = (p.yKeys as string[]) || []
      const data = (p.data as object[]) || []
      if (p.loading) return <div key={key} className="bf-chart-state">{renderLoadingSkeleton(4)}</div>
      if (!data.length) return <div key={key} className="bf-chart-state">{(p.emptyMessage as string) || 'No chart data available'}</div>
      return (
        <div key={key} className="bf-chart-container">
          {p.title && <div className="bf-chart-title">{p.title as string}</div>}
          <ResponsiveContainer width="100%" height={(p.height as number) || 300}>
            <LineChart data={data} onClick={(state) => p.click && ev('click', state?.activePayload?.[0]?.payload ?? {})}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={p.xKey as string} />
              <YAxis />
              <Tooltip />
              <Legend />
              {yKeys.map((yk, i) => (
                <Line key={yk} type="monotone" dataKey={yk} stroke={CHART_COLORS[i % CHART_COLORS.length]} strokeWidth={2} dot={false} />
              ))}
            </LineChart>
          </ResponsiveContainer>
        </div>
      )
    }

    case 'BarChart': {
      const yKeys = (p.yKeys as string[]) || []
      const data = (p.data as object[]) || []
      if (p.loading) return <div key={key} className="bf-chart-state">{renderLoadingSkeleton(4)}</div>
      if (!data.length) return <div key={key} className="bf-chart-state">{(p.emptyMessage as string) || 'No chart data available'}</div>
      return (
        <div key={key} className="bf-chart-container">
          {p.title && <div className="bf-chart-title">{p.title as string}</div>}
          <ResponsiveContainer width="100%" height={(p.height as number) || 300}>
            <BarChart data={data} layout={p.horizontal ? 'vertical' : 'horizontal'} onClick={(state) => p.click && ev('click', state?.activePayload?.[0]?.payload ?? {})}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey={p.horizontal ? undefined : p.xKey as string} type={p.horizontal ? 'number' : 'category'} />
              <YAxis dataKey={p.horizontal ? p.xKey as string : undefined} type={p.horizontal ? 'category' : 'number'} />
              <Tooltip />
              {yKeys.map((yk, i) => (
                <Bar key={yk} dataKey={yk} fill={CHART_COLORS[i % CHART_COLORS.length]} radius={[3, 3, 0, 0]} />
              ))}
            </BarChart>
          </ResponsiveContainer>
        </div>
      )
    }

    case 'DonutChart': {
      const data = (p.data as Array<{ [k: string]: unknown }>) || []
      const vk = (p.valueKey as string) || 'value'
      const lk = (p.labelKey as string) || 'label'
      if (p.loading) return <div key={key} className="bf-chart-state">{renderLoadingSkeleton(4)}</div>
      if (!data.length) return <div key={key} className="bf-chart-state">{(p.emptyMessage as string) || 'No chart data available'}</div>
      return (
        <div key={key} className="bf-chart-container">
          {p.title && <div className="bf-chart-title">{p.title as string}</div>}
          <ResponsiveContainer width="100%" height={(p.height as number) || 300}>
            <PieChart>
              <Pie data={data} cx="50%" cy="50%" innerRadius="55%" outerRadius="75%" dataKey={vk} nameKey={lk} paddingAngle={2} onClick={(payload) => p.click && ev('click', payload?.payload ?? {})}>
                {data.map((_, i) => <Cell key={i} fill={((p.colors as string[]) || [])[i] || CHART_COLORS[i % CHART_COLORS.length]} />)}
              </Pie>
              <Tooltip formatter={(value, name) => [value, name]} />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
        </div>
      )
    }

    case 'Toast':
      if (!p.visible) return null
      return (
        <div key={key} className={`bf-toast bf-toast-${(p.alertType as string) || 'info'}`}>
          {p.icon ? <Icon name={p.icon as string} size={16} /> : null}
          <div className="bf-toast-content">
            {p.title ? <div className="bf-toast-title">{p.title as string}</div> : null}
            <div className="bf-toast-message">{p.message as string}</div>
          </div>
        </div>
      )

    case 'Timeline':
      return (
        <div key={key} className="bf-timeline">
          {p.title ? <div className="bf-card-title" style={{ marginBottom: 12 }}>{p.title as string}</div> : null}
          {((p.items as Array<Record<string, any>>) || []).map((item, index) => (
            <div key={`${key}-timeline-${index}`} className="bf-timeline-item">
              <div className="bf-timeline-dot" />
              <div className="bf-timeline-content">
                <div className="bf-timeline-row">
                  <div className="bf-timeline-title">{String(item.title ?? '')}</div>
                  {item.time ? <div className="bf-timeline-time">{String(item.time)}</div> : null}
                </div>
                {item.subtitle ? <div className="bf-timeline-subtitle">{String(item.subtitle)}</div> : null}
                {item.description ? <div className="bf-timeline-description">{String(item.description)}</div> : null}
              </div>
            </div>
          ))}
        </div>
      )

    case 'SparklineStat':
      return <SparklineStatComponent key={key} props={p} />

    default:
      return (
        <div key={key} className={`bf-node-${type.toLowerCase()}`}>
          {renderChildren(children, ctx, key)}
        </div>
      )
  }
}

// ── Sub-components (need their own state) ─────────────────────────────────

function ToggleComponent({ props: p, dispatch }: { props: Record<string, any>; dispatch: (v: boolean) => void }) {
  const checked = Boolean(p.checked)
  return (
    <label
      className="bf-toggle-wrapper"
      onClick={() => {
        if (!p.disabled) dispatch(!checked)
      }}
    >
      <div className={`bf-toggle-switch ${checked ? 'checked' : ''}`} />
      {p.label as string}
    </label>
  )
}

function AnimatedValue({ value, animated }: { value: string; animated: boolean }) {
  const parseNumeric = (raw: string) => {
    const match = raw.match(/-?\d+(?:\.\d+)?/)
    if (!match) return null
    return {
      number: parseFloat(match[0]),
      prefix: raw.slice(0, match.index ?? 0),
      suffix: raw.slice((match.index ?? 0) + match[0].length),
      decimals: match[0].includes('.') ? match[0].split('.')[1].length : 0,
    }
  }

  const parsed = parseNumeric(value)
  const [display, setDisplay] = useState(() => {
    if (!animated || !parsed) return value
    return `${parsed.prefix}${(0).toFixed(parsed.decimals)}${parsed.suffix}`
  })

  useEffect(() => {
    if (!animated || !parsed) {
      setDisplay(value)
      return
    }

    const duration = 700
    const start = performance.now()

    let frame = 0
    const tick = (now: number) => {
      const progress = Math.min(1, (now - start) / duration)
      const eased = 1 - Math.pow(1 - progress, 3)
      const current = parsed.number * eased
      setDisplay(`${parsed.prefix}${current.toFixed(parsed.decimals)}${parsed.suffix}`)
      if (progress < 1) frame = requestAnimationFrame(tick)
    }

    frame = requestAnimationFrame(tick)
    return () => cancelAnimationFrame(frame)
  }, [animated, parsed?.decimals, parsed?.number, parsed?.prefix, parsed?.suffix, value])

  return <div className="bf-stat-value">{display}</div>
}

function DateRangePickerComponent({ props: p, dispatch }: { props: Record<string, any>; dispatch: (v: Record<string, string>) => void }) {
  const [start, setStart] = useState((p.start as string) || '')
  const [end, setEnd] = useState((p.end as string) || '')

  useEffect(() => {
    setStart((p.start as string) || '')
    setEnd((p.end as string) || '')
  }, [p.start, p.end])

  const emit = (nextStart: string, nextEnd: string) => dispatch({ start: nextStart, end: nextEnd })

  return (
    <div className="bf-form-field">
      {p.label && <label className="bf-label">{p.label as string}</label>}
      <div className="bf-date-range">
        <input
          className="bf-input"
          type="date"
          name={`${p.name as string}_start`}
          value={start}
          disabled={Boolean(p.disabled)}
          onChange={(e) => {
            const next = e.target.value
            setStart(next)
            emit(next, end)
          }}
        />
        <span className="bf-date-range-sep">to</span>
        <input
          className="bf-input"
          type="date"
          name={`${p.name as string}_end`}
          value={end}
          disabled={Boolean(p.disabled)}
          onChange={(e) => {
            const next = e.target.value
            setEnd(next)
            emit(start, next)
          }}
        />
      </div>
    </div>
  )
}

function MultiSelectComponent({ props: p, dispatch }: { props: Record<string, any>; dispatch: (v: string[]) => void }) {
  const selected = new Set(((p.values as string[]) || []).map(String))
  const options = (p.options as Array<{ label: string; value: string }>) || []

  const toggleValue = (value: string) => {
    if (selected.has(value)) selected.delete(value)
    else selected.add(value)
    dispatch(Array.from(selected))
  }

  return (
    <div className="bf-form-field">
      {p.label && <label className="bf-label">{p.label as string}</label>}
      <div className="bf-multiselect">
        {Array.from(selected).map((value) => (
          <input key={`hidden-${value}`} type="hidden" name={p.name as string} value={value} />
        ))}
        {options.map((option) => {
          const active = selected.has(option.value)
          return (
            <button
              key={option.value}
              type="button"
              className={`bf-multiselect-chip ${active ? 'active' : ''}`}
              disabled={Boolean(p.disabled)}
              onClick={() => toggleValue(option.value)}
            >
              {option.label}
            </button>
          )
        })}
      </div>
    </div>
  )
}

function AccordionComponent({ props: p, children, ctx, nodeKey }: { props: Record<string, any>; children: VNodeData[]; ctx: RenderCtx; nodeKey: string }) {
  const defaultOpen = ((p.defaultOpen as number[]) || []).map(Number)
  const [openItems, setOpenItems] = useState<number[]>(defaultOpen)
  const allowMultiple = Boolean(p.allowMultiple)

  const toggle = (index: number) => {
    setOpenItems((prev) => {
      if (prev.includes(index)) return prev.filter((item) => item !== index)
      if (allowMultiple) return [...prev, index]
      return [index]
    })
  }

  return (
    <div className="bf-accordion">
      {children.map((child, index) => {
        const cp = child.props as Record<string, any>
        const open = openItems.includes(index)
        return (
          <div key={`${nodeKey}-${index}`} className={`bf-accordion-item ${open ? 'open' : ''}`}>
            <button type="button" className="bf-accordion-trigger" onClick={() => toggle(index)}>
              <div className="bf-accordion-trigger-main">
                {cp.icon ? <Icon name={cp.icon as string} size={15} /> : null}
                <div>
                  <div className="bf-accordion-title">{cp.title as string}</div>
                  {cp.subtitle ? <div className="bf-accordion-subtitle">{cp.subtitle as string}</div> : null}
                </div>
              </div>
              <span className="bf-accordion-chevron">{open ? '−' : '+'}</span>
            </button>
            {open ? <div className="bf-accordion-content">{renderChildren(child.children, ctx, `${nodeKey}-accordion-${index}`)}</div> : null}
          </div>
        )
      })}
    </div>
  )
}

function SparklineStatComponent({ props: p }: { props: Record<string, any> }) {
  const color = (p.color as string) || 'var(--db-primary)'
  return (
    <div className="bf-sparkline-stat">
      <div className="bf-sparkline-header">
        <div className="bf-stat-label">{p.label as string}</div>
        {p.delta ? <div className={`bf-stat-delta ${((p.deltaType as string) || 'neutral')}`}>{p.delta as string}</div> : null}
      </div>
      <div className="bf-stat-value">{p.value as string}</div>
      <div className="bf-sparkline-chart">
        <ResponsiveContainer width="100%" height={70}>
          <LineChart data={(p.data as object[]) || []}>
            <Line dataKey={p.yKey as string} stroke={color} strokeWidth={2} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  )
}

function TableComponent({ props: p, dispatch }: { props: Record<string, any>; dispatch: RenderCtx['dispatch'] }) {
  const data = (p.data as Record<string, unknown>[]) || []
  const columns = (p.columns as Array<{ key: string; label: string; sortable?: boolean }>) || []
  const pageSize = (p.pagination as number) || 20
  const [page, setPage] = useState(0)
  const [sortKey, setSortKey] = useState<string | null>(null)
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc')

  let sorted = [...data]
  if (sortKey) {
    sorted.sort((a, b) => {
      const av = String(a[sortKey] ?? '')
      const bv = String(b[sortKey] ?? '')
      return sortDir === 'asc' ? av.localeCompare(bv, undefined, { numeric: true }) : bv.localeCompare(av, undefined, { numeric: true })
    })
  }

  const totalPages = Math.ceil(sorted.length / pageSize)
  const pageData = sorted.slice(page * pageSize, (page + 1) * pageSize)

  const handleSort = (key: string) => {
    if (sortKey === key) setSortDir(d => d === 'asc' ? 'desc' : 'asc')
    else { setSortKey(key); setSortDir('asc') }
    setPage(0)
  }

  const exportCsv = () => {
    const header = columns.map((col) => col.label).join(',')
    const rows = sorted.map((row) =>
      columns
        .map((col) => {
          const raw = String(row[col.key] ?? '')
          return `"${raw.replaceAll('"', '""')}"`
        })
        .join(',')
    )
    const csv = [header, ...rows].join('\n')
    const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' })
    const url = URL.createObjectURL(blob)
    const link = document.createElement('a')
    link.href = url
    link.download = 'brickflowui-table-export.csv'
    link.click()
    URL.revokeObjectURL(url)
  }

  if (p.loading) return (
    <div style={{ display: 'flex', justifyContent: 'center', padding: 40 }}>
      <div className="bf-spinner bf-spinner-lg" />
    </div>
  )

  if (!data.length) return (
    <div className="bf-table-empty">{p.emptyMessage as string || 'No data'}</div>
  )

  return (
    <div>
      {p.exportable && (
        <div className="bf-table-toolbar">
          <button type="button" className="bf-btn bf-btn-secondary" style={{ padding: '6px 12px', fontSize: 12 }} onClick={exportCsv}>
            Export CSV
          </button>
        </div>
      )}
      <div className="bf-table-wrapper">
        <table className="bf-table">
          <thead>
            <tr>
              {columns.map(col => (
                <th key={col.key} onClick={() => col.sortable && handleSort(col.key)}>
                  {col.label}
                  {col.sortable && sortKey === col.key && (sortDir === 'asc' ? ' ▲' : ' ▼')}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {pageData.map((row, ri) => {
              const rowClickId = (p as Record<string, unknown>).rowClick as string
              return (
                <tr key={ri} className={rowClickId ? 'clickable' : ''} onClick={() => rowClickId && dispatch(rowClickId, { row })}>
                  {columns.map(col => (
                    <td key={col.key} title={String(row[col.key] ?? '')}>
                      {String(row[col.key] ?? '')}
                    </td>
                  ))}
                </tr>
              )
            })}
          </tbody>
        </table>
      </div>
      {totalPages > 1 && (
        <div className="bf-table-pagination">
          <span>Showing {page * pageSize + 1}–{Math.min((page + 1) * pageSize, data.length)} of {data.length}</span>
          <div className="bf-table-pagination-controls">
            <button className="bf-btn bf-btn-secondary" style={{ padding: '4px 10px', fontSize: 12 }} disabled={page === 0} onClick={() => setPage(p => p - 1)}>← Prev</button>
            <button className="bf-btn bf-btn-secondary" style={{ padding: '4px 10px', fontSize: 12 }} disabled={page >= totalPages - 1} onClick={() => setPage(p => p + 1)}>Next →</button>
          </div>
        </div>
      )}
    </div>
  )
}

function TabsComponent({ props: p, children, ctx, nodeKey, dispatch }: { props: Record<string, any>; children: VNodeData[]; ctx: RenderCtx; nodeKey: string; dispatch: RenderCtx['dispatch'] }) {
  const [active, setActive] = useState((p.defaultActive as number) || 0)

  return (
    <div className="bf-tabs">
      <div className="bf-tabs-list">
        {children.map((child, i) => {
          const cp = child.props as Record<string, unknown>
          return (
            <button key={i} className={`bf-tab-trigger ${active === i ? 'active' : ''}`} onClick={() => {
              setActive(i)
              const changeId = p.change as string
              if (changeId) dispatch(changeId, { index: i })
            }}>
              {cp.icon ? <Icon name={cp.icon as string} size={14} /> : null}
              {cp.label as string}
            </button>
          )
        })}
      </div>
      <div className="bf-tab-content">
        {children[active]?.children && renderChildren(children[active].children, ctx, `${nodeKey}-tab-${active}`)}
      </div>
    </div>
  )
}
