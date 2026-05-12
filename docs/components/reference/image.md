# Image

## What It Does

`Image` renders local or remote images, screenshots, logos, avatars, and GIFs directly from Python.

## When To Use It

Use `Image` any time media is part of the product surface rather than an afterthought, especially for:

- logos in shell chrome
- inline product marks in heroes
- avatars in tables or chat
- screenshots in docs-style pages
- GIF demos inside examples

## Inputs To Know

- `src`
- `alt`
- `width`
- `height`
- `fit`
- `caption`
- `variant`
- `loading`

## Variants

Use the right variant for the job:

```python
db.Image("assets/logo.svg", alt="Logo", variant="inline")
db.Image("assets/user.png", alt="Operator", variant="avatar", width="40px")
db.Image("assets/screenshot.png", alt="Preview", variant="content")
```

- `content`: framed media surface for screenshots and larger images
- `inline`: shrink-to-content logo or mark with no frame styling
- `avatar`: circular small image for people or identities

## Local Files

Local image paths are served automatically by the runtime:

```python
db.Image("assets/brand/logo.svg", alt="Acme logo", variant="inline")
```

You do not need a separate static hosting setup just to display local images.

## Works Well With

`Hero`, `Sidebar`, `TopNav`, `Table`, `ChatMessage`, `Card`

## Notes

- Use `variant="inline"` for logos to avoid the heavier framed screenshot treatment.
- Use `variant="avatar"` when the media should feel like identity rather than content.
