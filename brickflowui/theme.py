import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Union

DEFAULT_THEME = {
    "branding": {
        "title": "BrickflowUI App",
        "logo": None,
        "favicon": None,
    },
    "colors": {
        "primary": "#003087",
        "primary-hover": "#00205b",
        "primary-light": "#00aed1",
        "bg": "#f8f9fa",
        "surface": "#ffffff",
        "text": "#1a1a1a",
        "text-muted": "#6b7280",
        "border": "#e5e7eb",
        "success": "#10b981",
        "warning": "#f59e0b",
        "error": "#ef4444",
        "link": "#003087",
    },
    "typography": {
        "sans": "'Inter', -apple-system, sans-serif",
        "mono": "'Fira Code', monospace",
        "base-size": "14px",
    },
    "spacing": {
        "base": "4px",
    },
    "radius": {
        "sm": "4px",
        "md": "8px",
        "lg": "12px",
    },
}

_SECTION_ALIASES = {
    "brand": "branding",
    "branding": "branding",
    "colors": "colors",
    "typography": "typography",
    "spacing": "spacing",
    "radius": "radius",
    "borders": "radius",
}

_KEY_ALIASES = {
    "branding": {
        "app_name": "title",
        "brand_name": "title",
        "name": "title",
    },
    "colors": {
        "primary_hover": "primary-hover",
        "primary_light": "primary-light",
        "background": "bg",
        "text_muted": "text-muted",
    },
    "typography": {
        "font_family": "sans",
        "font_mono": "mono",
        "base_size": "base-size",
    },
    "spacing": {
        "unit": "base",
    },
    "radius": {
        "radius": "md",
    },
}


class Theme:
    def __init__(self, theme_config: Union[str, Path, Dict[str, Any], None] = None):
        self.config = deepcopy(DEFAULT_THEME)
        if theme_config:
            self.load(theme_config)

    def load(self, theme_config: Union[str, Path, Dict[str, Any]]):
        if isinstance(theme_config, (str, Path)):
            path = Path(theme_config)
            if not path.exists():
                raise FileNotFoundError(f"Theme file not found: {path}")

            ext = path.suffix.lower()
            with open(path, "r", encoding="utf-8") as f:
                if ext == ".json":
                    content = json.load(f)
                elif ext in (".yaml", ".yml"):
                    try:
                        import yaml
                    except ImportError as exc:
                        raise ImportError(
                            "PyYAML is required to load YAML themes. "
                            "Install it with: pip install PyYAML"
                        ) from exc
                    content = yaml.safe_load(f)
                else:
                    raise ValueError(f"Unsupported theme format: {ext}")
            self._merge(self._normalize_theme(content))
        elif isinstance(theme_config, dict):
            self._merge(self._normalize_theme(theme_config))

    def branding_value(self, key: str, default: Any = None) -> Any:
        return self.config.get("branding", {}).get(key, default)

    def _merge(self, new_config: Dict[str, Any]):
        for section, values in new_config.items():
            if section in self.config and isinstance(self.config[section], dict):
                self.config[section].update(values)
            else:
                self.config[section] = values

    def _normalize_theme(self, raw_config: Mapping[str, Any]) -> Dict[str, Any]:
        normalized: Dict[str, Any] = {}
        for raw_section, raw_values in raw_config.items():
            section = _SECTION_ALIASES.get(raw_section, raw_section)
            if isinstance(raw_values, dict):
                section_aliases = _KEY_ALIASES.get(section, {})
                values = {
                    section_aliases.get(raw_key, raw_key): raw_value
                    for raw_key, raw_value in raw_values.items()
                }
            else:
                values = raw_values

            if section == "radius" and isinstance(values, dict) and "md" in values and "lg" not in values:
                values = {**values, "lg": values["md"]}

            if section in normalized and isinstance(normalized[section], dict) and isinstance(values, dict):
                normalized[section].update(values)
            else:
                normalized[section] = values
        return normalized

    def to_css_variables(self) -> str:
        """Generate CSS :root variables from the theme config."""
        lines = [":root {"]

        # Colors
        for key, val in self.config.get("colors", {}).items():
            lines.append(f"  --db-{key}: {val};")

        # Typography
        for key, val in self.config.get("typography", {}).items():
            lines.append(f"  --font-{key}: {val};")

        # Spacing
        base_spacing = self.config.get("spacing", {}).get("base", "4px")
        lines.append(f"  --space-unit: {base_spacing};")
        for i in range(1, 13):
            lines.append(f"  --space-{i}: calc(var(--space-unit) * {i});")

        # Radius
        for key, val in self.config.get("radius", {}).items():
            lines.append(f"  --radius-{key}: {val};")

        lines.append("}")
        return "\n".join(lines)
