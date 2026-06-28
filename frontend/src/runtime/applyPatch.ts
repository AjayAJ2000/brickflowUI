import type { Patch, VNodeData } from '../types'

export class PatchApplicationError extends Error {
  constructor(message: string) {
    super(message)
    this.name = 'PatchApplicationError'
  }
}

function requireNode(patch: Patch): VNodeData {
  if (!patch.node) throw new PatchApplicationError(`${patch.op} patch requires a node`)
  return patch.node
}

function requireIndex(index: number): void {
  if (!Number.isInteger(index) || index < 0) {
    throw new PatchApplicationError(`Invalid patch index: ${index}`)
  }
}

export function applyPatch(tree: VNodeData, patch: Patch): VNodeData {
  const { op, path, props } = patch

  if (path.length === 0) {
    if (op === 'replace') return requireNode(patch)
    if (op === 'update_props' && props) {
      const nextProps = { ...tree.props }
      for (const [key, value] of Object.entries(props)) {
        if (value === null) delete nextProps[key]
        else nextProps[key] = value
      }
      return { ...tree, props: nextProps }
    }
    throw new PatchApplicationError(`Invalid ${op} operation at the root path`)
  }

  const [index, ...rest] = path
  requireIndex(index)
  const nextChildren = [...tree.children]

  if (rest.length === 0) {
    if (op === 'insert') {
      if (index > nextChildren.length) {
        throw new PatchApplicationError(`Insert index ${index} is outside the child list`)
      }
      nextChildren.splice(index, 0, requireNode(patch))
      return { ...tree, children: nextChildren }
    }
    if (index >= nextChildren.length) {
      throw new PatchApplicationError(`Patch index ${index} is outside the child list`)
    }
    if (op === 'remove') {
      nextChildren.splice(index, 1)
      return { ...tree, children: nextChildren }
    }
    if (op === 'replace') {
      nextChildren[index] = requireNode(patch)
      return { ...tree, children: nextChildren }
    }
  }

  if (index >= nextChildren.length) {
    throw new PatchApplicationError(`Parent index ${index} is outside the child list`)
  }
  nextChildren[index] = applyPatch(nextChildren[index], { ...patch, path: rest })
  return { ...tree, children: nextChildren }
}

export function applyPatches(tree: VNodeData, patches: Patch[]): VNodeData {
  return patches.reduce((current, patch) => applyPatch(current, patch), tree)
}
