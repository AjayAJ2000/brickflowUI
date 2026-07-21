// @vitest-environment jsdom

import React, { act } from 'react'
import { createRoot, type Root } from 'react-dom/client'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import { Renderer } from './Renderer'
import type { VNodeData } from './types'

(globalThis as typeof globalThis & { IS_REACT_ACT_ENVIRONMENT: boolean }).IS_REACT_ACT_ENVIRONMENT = true

const modalNode: VNodeData = {
  type: 'Modal',
  props: {
    title: 'Executive brief',
    visible: true,
    size: 'md',
    close: 'close-modal',
  },
  children: [
    {
      type: 'Button',
      props: { label: 'Review details', click: 'review-details' },
      children: [],
      key: null,
    },
  ],
  key: null,
}

describe('Modal accessibility', () => {
  let container: HTMLDivElement
  let root: Root
  let trigger: HTMLButtonElement
  let dispatch: ReturnType<typeof vi.fn>

  beforeEach(() => {
    container = document.createElement('div')
    trigger = document.createElement('button')
    trigger.textContent = 'Open executive brief'
    document.body.append(trigger, container)
    trigger.focus()
    dispatch = vi.fn()
    root = createRoot(container)
  })

  afterEach(() => {
    act(() => root.unmount())
    document.body.replaceChildren()
  })

  function renderModal(node = modalNode) {
    act(() => {
      root.render(
        <Renderer
          node={node}
          dispatch={dispatch}
          navigate={vi.fn()}
          pendingEvents={new Map()}
          themeMode="light"
          setThemeMode={vi.fn()}
        />,
      )
    })
  }

  it('renders a labelled modal dialog and an accessible close control', () => {
    renderModal()

    const dialog = container.querySelector<HTMLElement>('[role="dialog"]')
    const title = container.querySelector<HTMLElement>('.bf-modal-title')
    const close = container.querySelector<HTMLButtonElement>('.bf-modal-close')
    const action = container.querySelector<HTMLButtonElement>('.bf-modal-body .bf-btn')

    expect(dialog).not.toBeNull()
    expect(dialog?.getAttribute('aria-modal')).toBe('true')
    expect(title?.id).toBeTruthy()
    expect(dialog?.getAttribute('aria-labelledby')).toBe(title?.id)
    expect(close?.getAttribute('aria-label')).toBe('Close Executive brief')
    expect(action?.dataset.bfFocusKey).toBe('review-details')
  })

  it('moves focus into the dialog and restores the trigger when the modal unmounts', () => {
    renderModal()

    const close = container.querySelector<HTMLButtonElement>('.bf-modal-close')
    expect(document.activeElement).toBe(close)

    renderModal({ type: 'Text', props: { value: 'Closed' }, children: [], key: null })
    expect(document.activeElement).toBe(trigger)
  })

  it('restores focus to a server-rendered replacement for the trigger', () => {
    trigger.dataset.bfFocusKey = 'open-executive-brief'
    renderModal()

    const replacement = document.createElement('button')
    replacement.textContent = trigger.textContent
    replacement.dataset.bfFocusKey = trigger.dataset.bfFocusKey
    trigger.replaceWith(replacement)
    trigger = replacement

    renderModal({ type: 'Text', props: { value: 'Closed' }, children: [], key: null })
    expect(document.activeElement).toBe(replacement)
  })

  it('captures the trigger before an opening patch replaces it', () => {
    function ModalFlow() {
      const [open, setOpen] = React.useState(false)
      const node: VNodeData = open
        ? {
            type: 'Column',
            props: {},
            children: [
              {
                type: 'Button',
                props: { label: 'Executive brief', click: 'open-replacement' },
                children: [],
                key: null,
              },
              modalNode,
            ],
            key: null,
          }
        : {
            type: 'Button',
            props: { label: 'Executive brief', click: 'open-initial' },
            children: [],
            key: null,
          }

      return (
        <Renderer
          node={node}
          dispatch={(eventId) => {
            if (eventId.startsWith('open-')) setOpen(true)
            if (eventId === 'close-modal') setOpen(false)
          }}
          navigate={vi.fn()}
          pendingEvents={new Map()}
          themeMode="light"
          setThemeMode={vi.fn()}
        />
      )
    }

    act(() => root.render(<ModalFlow />))
    const openingTrigger = container.querySelector<HTMLButtonElement>('.bf-btn')
    openingTrigger?.focus()
    act(() => openingTrigger?.click())

    expect(openingTrigger?.isConnected).toBe(false)
    const close = container.querySelector<HTMLButtonElement>('.bf-modal-close')
    expect(document.activeElement).toBe(close)

    act(() => close?.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })))
    const replacement = container.querySelector<HTMLButtonElement>('.bf-btn')
    expect(replacement).not.toBe(openingTrigger)
    expect(document.activeElement).toBe(replacement)
  })

  it('dispatches close on Escape and contains Tab focus within the dialog', () => {
    renderModal()

    const close = container.querySelector<HTMLButtonElement>('.bf-modal-close')
    const action = container.querySelector<HTMLButtonElement>('.bf-modal-body .bf-btn')
    expect(close).not.toBeNull()
    expect(action).not.toBeNull()

    action?.focus()
    act(() => action?.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab', bubbles: true })))
    expect(document.activeElement).toBe(close)

    act(() => close?.dispatchEvent(new KeyboardEvent('keydown', { key: 'Tab', shiftKey: true, bubbles: true })))
    expect(document.activeElement).toBe(action)

    act(() => action?.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true })))
    expect(dispatch).toHaveBeenCalledWith('close-modal', {})
  })
})
