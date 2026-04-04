from pathlib import Path

from brickflowui.app import App
from brickflowui.theme import Theme


def test_theme_normalizes_branding_and_alias_keys():
    theme = Theme(
        {
            "branding": {
                "app_name": "Acme Portal",
                "logo": "/static/acme.svg",
                "favicon": "/static/acme.ico",
            },
            "colors": {
                "background": "#ffffff",
                "primary_hover": "#123456",
                "text_muted": "#666666",
            },
            "typography": {
                "font_family": "'IBM Plex Sans', sans-serif",
                "base_size": "15px",
            },
            "spacing": {
                "unit": "6px",
            },
            "borders": {
                "radius": "14px",
            },
        }
    )

    assert theme.branding_value("title") == "Acme Portal"
    assert theme.branding_value("logo") == "/static/acme.svg"
    assert theme.config["colors"]["bg"] == "#ffffff"
    assert theme.config["colors"]["primary-hover"] == "#123456"
    assert theme.config["typography"]["sans"] == "'IBM Plex Sans', sans-serif"
    assert theme.config["spacing"]["base"] == "6px"
    assert theme.config["radius"]["md"] == "14px"


def test_app_uses_branding_from_theme_file_when_defaults_are_used():
    theme_path = Path(__file__).parent / "_branding_test.yaml"
    try:
        theme_path.write_text(
            "\n".join(
                [
                    "branding:",
                    "  title: Acme Control Center",
                    "  logo: /branding/acme.svg",
                    "  favicon: /branding/acme.ico",
                ]
            ),
            encoding="utf-8",
        )

        app = App(theme=theme_path)

        assert app.title == "Acme Control Center"
        assert app.logo == "/branding/acme.svg"
        assert app.favicon == "/branding/acme.ico"
    finally:
        if theme_path.exists():
            try:
                theme_path.unlink()
            except PermissionError:
                pass
