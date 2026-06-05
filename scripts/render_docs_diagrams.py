from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

from PIL import Image, ImageColor, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "docs" / "assets"


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/Inter-Bold.ttf") if bold else Path("C:/Windows/Fonts/Inter-Regular.ttf"),
        Path("C:/Windows/Fonts/seguisb.ttf") if bold else Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arialbd.ttf") if bold else Path("C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


FONT_H1 = load_font(44, bold=True)
FONT_H2 = load_font(30, bold=True)
FONT_H3 = load_font(24, bold=True)
FONT_BODY = load_font(18, bold=False)
FONT_BODY_BOLD = load_font(18, bold=True)
FONT_CAPTION = load_font(16, bold=False)
FONT_SMALL = load_font(14, bold=False)


BG_LIGHT = "#F4F7FD"
PANEL_LIGHT = "#FFFFFF"
BORDER_LIGHT = "#D9E3F3"
TEXT_DARK = "#0F172A"
TEXT_MUTED = "#526176"
ACCENT = "#4E6CFF"
ACCENT_SOFT = "#EAF0FF"
SUCCESS = "#15803D"
ERROR = "#BE123C"

BG_DARK = "#0B1324"
PANEL_DARK = "#111D33"
BORDER_DARK = "#29457F"
TEXT_LIGHT = "#F8FAFC"
TEXT_SOFT = "#A7B6D6"


def rounded_panel(draw: ImageDraw.ImageDraw, xy, fill, outline, radius=28, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def shadowed_panel(base: Image.Image, xy, fill, outline, radius=28, shadow=(0, 20, 28, "#8AA0C840"), width=2):
    x1, y1, x2, y2 = xy
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    layer_draw = ImageDraw.Draw(layer)
    sx, sy, blur, color = shadow
    layer_draw.rounded_rectangle((x1 + sx, y1 + sy, x2 + sx, y2 + sy), radius=radius, fill=ImageColor.getrgb(color))
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(layer)
    draw = ImageDraw.Draw(base)
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def text_box(draw: ImageDraw.ImageDraw, text: str, box: tuple[int, int, int, int], font, fill, line_gap=8):
    x1, y1, x2, y2 = box
    max_width = x2 - x1
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = word if not current else f"{current} {word}"
        if draw.textlength(trial, font=font) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)

    y = y1
    for line in lines:
        draw.text((x1, y), line, font=font, fill=fill)
        bbox = draw.textbbox((x1, y), line, font=font)
        y = bbox[3] + line_gap
        if y > y2:
            break
    return y


def bullet_list(draw: ImageDraw.ImageDraw, items: Sequence[str], x: int, y: int, width: int, fill, font=FONT_BODY, gap=10):
    for item in items:
        draw.text((x, y), "•", font=font, fill=fill)
        y = text_box(draw, item, (x + 18, y, x + width, y + 80), font, fill, line_gap=6) + gap
    return y


def arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color=ACCENT, width=10):
    draw.line([start, end], fill=color, width=width)
    ex, ey = end
    draw.polygon([(ex, ey), (ex - 18, ey - 10), (ex - 18, ey + 10)], fill=color)


def curve(draw: ImageDraw.ImageDraw, points: Sequence[tuple[int, int]], color=ACCENT, width=8):
    draw.line(points, fill=color, width=width, joint="curve")


def canvas(width=2400, height=1400, dark=False):
    bg = BG_DARK if dark else BG_LIGHT
    image = Image.new("RGBA", (width, height), ImageColor.getrgb(bg))
    return image, ImageDraw.Draw(image)


@dataclass
class Card:
    title: str
    body: str
    bullets: Sequence[str]


def card_block(base: Image.Image, draw: ImageDraw.ImageDraw, xy, card: Card, dark=False, step: str | None = None):
    fill = PANEL_DARK if dark else PANEL_LIGHT
    outline = BORDER_DARK if dark else BORDER_LIGHT
    t_primary = TEXT_LIGHT if dark else TEXT_DARK
    t_muted = TEXT_SOFT if dark else TEXT_MUTED
    shadowed_panel(base, xy, fill, outline, radius=30, shadow=(0, 18, 18, "#00000040" if dark else "#93A9CF40"))
    x1, y1, x2, y2 = xy
    if step:
        draw.rounded_rectangle((x1 + 26, y1 + 24, x1 + 82, y1 + 66), radius=21, fill=ACCENT_SOFT if not dark else "#1C2A4D")
        draw.text((x1 + 45, y1 + 34), step, font=FONT_BODY_BOLD, fill=ACCENT)
        title_x = x1 + 102
    else:
        title_x = x1 + 30
    draw.text((title_x, y1 + 26), card.title, font=FONT_H2, fill=t_primary)
    next_y = text_box(draw, card.body, (x1 + 30, y1 + 82, x2 - 28, y1 + 180), FONT_BODY, t_muted, line_gap=8) + 12
    bullet_list(draw, card.bullets, x1 + 30, next_y, x2 - x1 - 60, t_muted, font=FONT_CAPTION, gap=8)


def render_runtime():
    image, draw = canvas(dark=True)
    draw.text((88, 88), "Runtime and Render Lifecycle", font=FONT_H1, fill=TEXT_LIGHT)
    text_box(
        draw,
        "The core BrickflowUI loop: Python builds the VNode tree, the runtime tracks state and auth, websocket messages carry patches, and the renderer preserves the user's interaction context.",
        (88, 150, 2100, 240),
        FONT_BODY,
        TEXT_SOFT,
    )
    rounded_panel(draw, (72, 240, 2328, 1260), "#0E172A", "#223B70", radius=34, width=2)

    cards = [
        Card("Python page", "App functions compose VNodes from session state, route context, backend data, and component props.", ["layouts, hero blocks, shell primitives", "tables, charts, forms, media"]),
        Card("Runtime core", "The server normalizes the tree, resolves auth, serves local assets, and tracks dirty rerenders.", ["session state and event registry", "loading bootstrap and route handlers"]),
        Card("Websocket wire", "Initial render sends a full tree. Interactive updates send event payloads and return patches or completion markers.", ["full tree on connect", "patch diffs after state changes"]),
        Card("React renderer", "Frontend components keep text input local-first, preserve focus and scroll, and apply shell theming and motion.", ["local-first controlled inputs", "smooth patch application"]),
    ]
    positions = [(150, 360, 620, 760), (680, 360, 1150, 760), (1210, 360, 1680, 760), (1740, 360, 2210, 760)]
    for index, (pos, card) in enumerate(zip(positions, cards), start=1):
        card_block(image, draw, pos, card, dark=True, step=str(index))

    arrow(draw, (620, 560), (680, 560))
    arrow(draw, (1150, 560), (1210, 560))
    arrow(draw, (1680, 560), (1740, 560))
    curve(draw, [(450, 840), (620, 980), (930, 1080), (1210, 1080), (1510, 980), (1780, 840)], color="#6E88FF", width=10)
    draw.text((760, 1120), "User events flow back to Python, mutate state, and trigger the next patch cycle.", font=FONT_H3, fill="#DCE8FF")
    image.save(ASSETS / "runtime-flow.png", optimize=True)


def render_auth():
    image, draw = canvas()
    draw.text((88, 88), "Authentication and Guard Flow", font=FONT_H1, fill=TEXT_DARK)
    text_box(
        draw,
        "How BrickflowUI resolves identity, evaluates route and page policies, and decides whether the request, websocket session, or handler is allowed to continue.",
        (88, 150, 2140, 240),
        FONT_BODY,
        TEXT_MUTED,
    )
    rounded_panel(draw, (72, 240, 2328, 1260), "#FFFFFF90", "#D7E3F8", radius=34, width=2)

    cards = [
        Card("Entry point", "A browser request, websocket connection, or form/API call arrives at the runtime.", ["method, path, headers, cookies available", "request context attached early"]),
        Card("Auth provider", "The configured provider resolves a principal from headers, session cookies, or platform SSO.", ["app principal", "user principal", "anonymous fallback"]),
        Card("Policy evaluation", "Route or page access rules check the principal type and any required role claims.", ["public / authenticated / user / app", "optional role enforcement"]),
        Card("Outcome", "Authorized flows continue to rendering or handler execution. Denied flows return clear sign-in or access-denied feedback.", ["role-aware shell navigation", "consistent failure modes"]),
    ]
    positions = [(130, 360, 650, 760), (690, 360, 1210, 760), (1250, 360, 1770, 760), (1810, 360, 2290, 760)]
    for index, (pos, card) in enumerate(zip(positions, cards), start=1):
        card_block(image, draw, pos, card, dark=False, step=str(index))
    arrow(draw, (650, 560), (690, 560))
    arrow(draw, (1210, 560), (1250, 560))
    arrow(draw, (1770, 560), (1810, 560))

    rounded_panel(draw, (130, 860, 2290, 1180), PANEL_DARK, "#284780", radius=32, width=2)
    draw.text((180, 920), "Enterprise checkpoints", font=FONT_H2, fill=TEXT_LIGHT)
    sections = [
        ("Identity source", "Start with HeaderAuthProvider locally, then swap to enterprise SSO, session auth, or platform-native identity."),
        ("Navigation filtering", "Unauthorized pages are hidden from shell navigation so users do not discover dead-end routes."),
        ("Audit hooks", "Optional audit logging gives you an event trail for protected actions and route access decisions."),
        ("Failure experience", "Denied requests should still feel product-grade: clear sign-in required or access denied messaging."),
    ]
    x = 180
    for title, body in sections:
        rounded_panel(draw, (x, 980, x + 480, 1130), "#13213A", "#284780", radius=24, width=2)
        draw.text((x + 24, 1016), title, font=FONT_H3, fill="#E5EDFF")
        text_box(draw, body, (x + 24, 1052, x + 450, 1114), FONT_CAPTION, "#AFC1E4", line_gap=6)
        x += 520
    image.save(ASSETS / "auth-guard-flow.png", optimize=True)


def render_theme():
    image, draw = canvas()
    draw.text((88, 88), "Theme System and Visual Presets", font=FONT_H1, fill=TEXT_DARK)
    text_box(
        draw,
        "Branding, semantic tokens, presets, and light or dark overrides all flow through one normalization layer so shell, charts, tables, and loading states stay visually coherent.",
        (88, 150, 2140, 240),
        FONT_BODY,
        TEXT_MUTED,
    )
    rounded_panel(draw, (72, 240, 2328, 1260), "#FFFFFF90", "#D7E3F8", radius=34, width=2)

    top_cards = [
        Card("Theme input", "Python or YAML theme defines branding, loading assets, light and dark mode overrides, and an optional preset.", ["logo, favicon, tagline", "light / dark sections", "loading image, GIF, or video"]),
        Card("Normalization", "Aliases resolve into canonical token names. Presets are applied first, then explicit user tokens override them.", ["background → bg", "light → light_mode", "preset layering"]),
        Card("Runtime tokens", "Resolved values become CSS variables and loading config used by the frontend shell and components.", ["colors and surfaces", "spacing, radius, shadows", "motion and loading modes"]),
        Card("UI output", "The same token set powers nav, cards, charts, tables, overlays, loading, and dark or light mode switching.", ["shared shell language", "mode-aware loading visuals"]),
    ]
    positions = [(120, 340, 620, 760), (660, 340, 1160, 760), (1200, 340, 1700, 760), (1740, 340, 2240, 760)]
    for index, (pos, card) in enumerate(zip(positions, top_cards), start=1):
        card_block(image, draw, pos, card, dark=False, step=str(index))
    arrow(draw, (620, 560), (660, 560))
    arrow(draw, (1160, 560), (1200, 560))
    arrow(draw, (1700, 560), (1740, 560))

    rounded_panel(draw, (120, 840, 1080, 1180), PANEL_DARK, "#284780", radius=30, width=2)
    draw.text((168, 900), "Preset families", font=FONT_H2, fill=TEXT_LIGHT)
    presets = [
        ("Modern", "#FFFFFF", TEXT_DARK, "balanced default"),
        ("Executive", "#EEF2FF", "#1E3A8A", "board-ready clarity"),
        ("Bento", "#FAF5FF", "#6D28D9", "editorial card rhythm"),
        ("Cyberpunk", "#07101F", "#67E8F9", "high-contrast ops room"),
        ("Minimal", "#F8FAFC", TEXT_DARK, "quiet utility surfaces"),
    ]
    x = 168
    for title, fill, text_fill, note in presets:
        rounded_panel(draw, (x, 960, x + 150, 1128), fill, "#D7E3F8" if fill != "#07101F" else "#294780", radius=24, width=2)
        draw.text((x + 24, 1008), title, font=FONT_H3, fill=text_fill)
        text_box(draw, note, (x + 24, 1050, x + 126, 1110), FONT_SMALL, text_fill if fill == "#07101F" else TEXT_MUTED, line_gap=4)
        x += 178

    rounded_panel(draw, (1140, 840, 2240, 1180), PANEL_LIGHT, BORDER_LIGHT, radius=30, width=2)
    draw.text((1188, 900), "Mode-aware loading and branding", font=FONT_H2, fill=TEXT_DARK)
    rounded_panel(draw, (1188, 970, 1658, 1128), "#F8FAFC", "#D7E3F8", radius=24, width=2)
    draw.text((1224, 1012), "Light mode", font=FONT_H3, fill=TEXT_DARK)
    text_box(draw, "Use bright logos, crisp neutral backgrounds, and loader copy that feels clear and business-ready.", (1224, 1052, 1628, 1110), FONT_CAPTION, TEXT_MUTED, line_gap=6)
    rounded_panel(draw, (1700, 970, 2200, 1128), "#0F172A", "#284780", radius=24, width=2)
    draw.text((1736, 1012), "Dark mode", font=FONT_H3, fill=TEXT_LIGHT)
    text_box(draw, "Swap in darker media or alternate loader assets so brand marks stay legible and intentional.", (1736, 1052, 2168, 1110), FONT_CAPTION, TEXT_SOFT, line_gap=6)
    image.save(ASSETS / "theme-system.png", optimize=True)


def render_deployment():
    image, draw = canvas(dark=True)
    draw.text((88, 88), "Deployment Topology", font=FONT_H1, fill=TEXT_LIGHT)
    text_box(
        draw,
        "A practical enterprise deployment map for BrickflowUI: client traffic enters through the platform edge, reaches the app runtime, and fans out to shared state, data systems, and observability services.",
        (88, 150, 2140, 240),
        FONT_BODY,
        TEXT_SOFT,
    )
    rounded_panel(draw, (72, 240, 2328, 1260), "#0E172A", "#223B70", radius=34, width=2)

    blocks = [
        ((160, 520, 520, 800), Card("Browser", "Desktop, tablet, and mobile clients consume the shell and keep a websocket session open for stateful interaction.", ["responsive shell", "forms, charts, tables", "theme toggles and loading states"])),
        ((680, 320, 1120, 560), Card("Ingress / Databricks App", "Platform edge handles routing, TLS, sticky session behavior, and app hosting semantics.", ["host and port resolution", "edge security policies"])),
        ((680, 640, 1120, 940), Card("BrickflowUI runtime", "FastAPI + Uvicorn serve the shell, resolve auth, manage state, and run page and route handlers.", ["websocket sessions", "asset URLs and loading bootstrap", "route + guard enforcement"])),
        ((1280, 300, 1740, 560), Card("Shared state", "Add Redis or another shared store when you need coordination across multiple app instances.", ["session coordination", "future scale-out path"])),
        ((1280, 640, 1740, 940), Card("Warehouse and APIs", "Query Databricks SQL, Unity Catalog, internal services, or model endpoints from backend handlers.", ["secure data access", "controlled server-side queries"])),
        ((1880, 520, 2260, 800), Card("Logs and metrics", "Collect request latency, event audit trails, error rates, and health signals for supportability.", ["traceable runtime behavior", "enterprise operations readiness"])),
    ]
    for i, (xy, card) in enumerate(blocks, start=1):
        card_block(image, draw, xy, card, dark=True, step=str(i))

    arrow(draw, (520, 660), (680, 660))
    arrow(draw, (1120, 430), (1280, 430))
    arrow(draw, (1120, 790), (1280, 790))
    arrow(draw, (1740, 660), (1880, 660))
    draw.text((1170, 414), "shared session path", font=FONT_SMALL, fill="#9FB2FF")
    draw.text((1170, 774), "data and service path", font=FONT_SMALL, fill="#9FB2FF")

    rounded_panel(draw, (160, 1040, 2260, 1188), "#13213A", "#294780", radius=26, width=2)
    draw.text((210, 1092), "Recommended rollout path", font=FONT_H3, fill=TEXT_LIGHT)
    text_box(
        draw,
        "Start with a single runtime or sticky-session deployment. Add shared state only when traffic or multi-instance coordination makes it necessary, then layer centralized observability and governance controls.",
        (210, 1132, 2200, 1180),
        FONT_CAPTION,
        TEXT_SOFT,
        line_gap=6,
    )
    image.save(ASSETS / "deployment-topology.png", optimize=True)


def main():
    ASSETS.mkdir(parents=True, exist_ok=True)
    render_runtime()
    render_auth()
    render_theme()
    render_deployment()
    print("Rendered PNG documentation diagrams.")


if __name__ == "__main__":
    main()
