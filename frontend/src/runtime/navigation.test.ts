import { describe, expect, it } from 'vitest'

import { navigationAction } from './navigation'

describe('navigationAction', () => {
  it('pushes history for user navigation', () => {
    expect(navigationAction('/reports?status=open#latest', 'user')).toEqual({
      message: { type: 'navigate', path: '/reports?status=open#latest' },
      history: 'push',
    })
  })

  it('does not mutate history for popstate synchronization', () => {
    expect(navigationAction('/home', 'popstate')).toEqual({
      message: { type: 'navigate', path: '/home' },
      history: 'none',
    })
  })
})
