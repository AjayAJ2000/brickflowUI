// Type definitions for the BrickflowUI VNode wire protocol

export interface VNodeData {
  type: string
  props: Record<string, unknown>
  children: VNodeData[]
  key: string | null
}

export interface FullMessage {
  type: 'full'
  tree: VNodeData
}

export interface PatchMessage {
  type: 'patch'
  patches: Patch[]
}

export interface ErrorMessage {
  type: 'error'
  message: string
}

export type ServerMessage = FullMessage | PatchMessage | ErrorMessage

export interface Patch {
  op: 'replace' | 'update_props' | 'insert' | 'remove'
  path: number[]
  node?: VNodeData
  props?: Record<string, unknown>
}

export interface ClientEvent {
  type: 'event'
  event_id: string
  data: Record<string, unknown>
}

export interface ClientNavigate {
  type: 'navigate'
  path: string
}
