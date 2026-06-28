import { describe, expect, it } from 'vitest'

import { shouldSubmitChatInput } from './chat'

describe('shouldSubmitChatInput', () => {
  it('submits an ordinary Enter key', () => {
    expect(shouldSubmitChatInput('Enter', false)).toBe(true)
  })

  it('does not submit Enter during IME composition', () => {
    expect(shouldSubmitChatInput('Enter', true)).toBe(false)
  })

  it('does not submit other keys', () => {
    expect(shouldSubmitChatInput('a', false)).toBe(false)
  })
})
