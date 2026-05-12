import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Union


DEFAULT_THEME = {
    "default_mode": "dark",
    "branding": {
        "title": "BrickflowUI App",
        "tagline": "React components. Python syntax.",
        "logo": None,
        "favicon": None,
        "show_theme_toggle": True,
    },
    "loading": {
        "title": "BrickflowUI",
        "message": "Connecting to runtime...",
        "subtitle": "Preparing the workspace runtime.",
        "animation": "spinner",
    },
    "colors": {
        "primary": "#4361EE",
        "primary-hover": "#3650D8",
        "primary-light": "rgba(67, 97, 238, 0.18)",
        "bg": "#0A0F1E",
        "surface": "#0F172A",
        "surface-2": "#1E293B",
        "text": "#F1F5F9",
        "text-muted": "#94A3B8",
        "text-subtle": "#64748B",
        "border": "#1E293B",
        "border-strong": "#334155",
        "success": "#22C55E",
        "warning": "#F59E0B",
        "error": "#F43F5E",
        "info": "#3B82F6",
        "link": "#4361EE",
    },
    "surfaces": {
        "canvas": "#0A0F1E",
        "muted": "#111B2E",
        "overlay": "rgba(10, 15, 30, 0.82)",
        "card": "#1E293B",
        "hover": "#334155",
    },
    "typography": {
        "sans": "'Inter', 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "heading": "'Plus Jakarta Sans', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif",
        "mono": "'JetBrains Mono', 'Fira Code', Menlo, Monaco, monospace",
        "base-size": "15px",
    },
    "spacing": {
        "base": "4px",
    },
    "radius": {
        "sm": "4px",
        "md": "6px",
        "lg": "8px",
        "xl": "12px",
        "full": "9999px",
    },
    "shadows": {
        "sm": "0 0 0 1px rgba(51, 65, 85, 0.48)",
        "md": "0 0 0 1px rgba(51, 65, 85, 0.72)",
        "lg": "0 0 0 1px rgba(67, 97, 238, 0.12), 0 24px 48px rgba(2, 6, 23, 0.48)",
    },
    "motion": {
        "duration-fast": "140ms",
        "duration-normal": "220ms",
        "duration-slow": "360ms",
        "easing-standard": "cubic-bezier(0.2, 0.8, 0.2, 1)",
        "stagger-step": "40ms",
    },
    "modes": {
        "dark": {},
        "light": {
            "colors": {
                "primary": "#4361EE",
                "primary-hover": "#3650D8",
                "primary-light": "rgba(67, 97, 238, 0.12)",
                "bg": "#F8FAFC",
                "surface": "#FFFFFF",
                "surface-2": "#F1F5F9",
                "text": "#0F172A",
                "text-muted": "#475569",
                "text-subtle": "#94A3B8",
                "border": "#E2E8F0",
                "border-strong": "#CBD5E1",
                "success": "#15803D",
                "warning": "#B45309",
                "error": "#BE123C",
                "info": "#1D4ED8",
                "link": "#4361EE",
            },
            "surfaces": {
                "canvas": "#F8FAFC",
                "muted": "#F1F5F9",
                "overlay": "rgba(255, 255, 255, 0.84)",
                "card": "#F1F5F9",
                "hover": "#E2E8F0",
            },
            "shadows": {
                "sm": "0 1px 2px rgba(15, 23, 42, 0.05)",
                "md": "0 8px 24px rgba(15, 23, 42, 0.08)",
                "lg": "0 24px 48px rgba(15, 23, 42, 0.12)",
            },
        },
    },
}


_SECTION_ALIASES = {
    "brand": "branding",
    "branding": "branding",
    "colors": "colors",
    "loading": "loading",
    "typography": "typography",
    "spacing": "spacing",
    "radius": "radius",
    "borders": "radius",
    "surfaces": "surfaces",
    "shadows": "shadows",
    "motion": "motion",
    "modes": "modes",
    "light_mode": "light_mode",
    "dark_mode": "dark_mode",
}

_KEY_ALIASES = {
    "branding": {
        "app_name": "title",
        "brand_name": "title",
        "name": "title",
        "brand_tagline": "tagline",
        "subtitle": "tagline",
        "theme_toggle": "show_theme_toggle",
    },
    "colors": {
        "primary_hover": "primary-hover",
        "primary_light": "primary-light",
        "background": "bg",
        "text_muted": "text-muted",
        "text_subtle": "text-subtle",
        "border_strong": "border-strong",
    },
    "typography": {
        "font_family": "sans",
        "font_heading": "heading",
        "font_mono": "mono",
        "base_size": "base-size",
    },
    "spacing": {
        "unit": "base",
    },
    "radius": {
        "radius": "md",
    },
    "surfaces": {
        "background": "canvas",
        "surface": "muted",
    },
    "shadows": {
        "small": "sm",
        "medium": "md",
        "large": "lg",
    },
    "motion": {
        "duration_fast": "duration-fast",
        "duration_normal": "duration-normal",
        "duration_slow": "duration-slow",
        "easing_standard": "easing-standard",
        "stagger_step": "stagger-step",
    },
}


def _deep_merge(base: Dict[str, Any], override: Mapping[str, Any]) -> Dict[str, Any]:
    merged = deepcopy(base)
    for key, value in override.items():
        if isinstance(value, Mapping) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = deepcopy(value)
    return merged


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

    def default_mode(self) -> str:
        mode = str(self.config.get("default_mode", "dark")).lower()
        return mode if mode in {"light", "dark"} else "dark"

    def branding_value(self, key: str, default: Any = None) -> Any:
        return self.config.get("branding", {}).get(key, default)

    def _merge(self, new_config: Dict[str, Any]):
        self.config = _deep_merge(self.config, new_config)

    def _normalize_section_values(self, section: str, raw_values: Any) -> Any:
        if not isinstance(raw_values, dict):
            return raw_values

        section_aliases = _KEY_ALIASES.get(section, {})
        values = {
            section_aliases.get(raw_key, raw_key): raw_value
            for raw_key, raw_value in raw_values.items()
        }

        if section == "radius" and "md" in values and "lg" not in values:
            values = {**values, "lg": values["md"]}
        return values

    def _normalize_modes(self, raw_modes: Mapping[str, Any]) -> Dict[str, Any]:
        normalized_modes: Dict[str, Any] = {}
        for mode_name, mode_values in raw_modes.items():
            if not isinstance(mode_values, Mapping):
                continue
            normalized_mode: Dict[str, Any] = {}
            for section_name, section_values in mode_values.items():
                section = _SECTION_ALIASES.get(section_name, section_name)
                normalized_mode[section] = self._normalize_section_values(section, section_values)
            normalized_modes[str(mode_name).lower()] = normalized_mode
        return normalized_modes

    def _normalize_theme(self, raw_config: Mapping[str, Any]) -> Dict[str, Any]:
        normalized: Dict[str, Any] = {}
        for raw_section, raw_values in raw_config.items():
            section = _SECTION_ALIASES.get(raw_section, raw_section)

            if section == "modes" and isinstance(raw_values, Mapping):
                normalized["modes"] = self._normalize_modes(raw_values)
                continue

            if section in {"light_mode", "dark_mode"} and isinstance(raw_values, Mapping):
                modes = normalized.setdefault("modes", {})
                mode_name = "light" if section == "light_mode" else "dark"
                modes[mode_name] = {
                    _SECTION_ALIASES.get(mode_section, mode_section): self._normalize_section_values(
                        _SECTION_ALIASES.get(mode_section, mode_section),
                        mode_values,
                    )
                    for mode_section, mode_values in raw_values.items()
                }
                continue

            values = self._normalize_section_values(section, raw_values)

            if section in normalized and isinstance(normalized[section], dict) and isinstance(values, dict):
                normalized[section].update(values)
            else:
                normalized[section] = values
        return normalized

    def _resolved_mode_config(self, mode: Optional[str] = None) -> Dict[str, Any]:
        selected_mode = (mode or self.default_mode()).lower()
        mode_overrides = self.config.get("modes", {}).get(selected_mode, {})
        merged = deepcopy(self.config)
        merged.pop("modes", None)
        merged.pop("default_mode", None)
        return _deep_merge(merged, mode_overrides)

    def _css_block(self, selector: str, config: Mapping[str, Any]) -> str:
        lines = [f"{selector} {{"]

        for key, val in config.get("colors", {}).items():
            lines.append(f"  --db-{key}: {val};")

        for key, val in config.get("surfaces", {}).items():
            lines.append(f"  --db-surface-{key}: {val};")

        for key, val in config.get("typography", {}).items():
            lines.append(f"  --font-{key}: {val};")

        base_spacing = config.get("spacing", {}).get("base", "4px")
        lines.append(f"  --space-unit: {base_spacing};")
        for i in range(1, 13):
            lines.append(f"  --space-{i}: calc(var(--space-unit) * {i});")

        for key, val in config.get("radius", {}).items():
            lines.append(f"  --radius-{key}: {val};")

        for key, val in config.get("shadows", {}).items():
            lines.append(f"  --shadow-{key}: {val};")

        motion = config.get("motion", {})
        for key, val in motion.items():
            lines.append(f"  --motion-{key}: {val};")

        if "duration-normal" in motion:
            lines.append(f"  --transition-duration: {motion['duration-normal']};")
        if "easing-standard" in motion:
            lines.append(f"  --transition-easing: {motion['easing-standard']};")
        if "duration-normal" in motion and "easing-standard" in motion:
            lines.append("  --transition: var(--transition-duration) var(--transition-easing);")

        lines.append("}")
        return "\n".join(lines)

    def to_css_variables(self) -> str:
        default_mode = self.default_mode()
        blocks = [self._css_block(":root", self._resolved_mode_config(default_mode))]
        for mode_name in ("dark", "light"):
            if mode_name == default_mode:
                continue
            blocks.append(
                self._css_block(
                    f":root[data-theme-mode='{mode_name}']",
                    self._resolved_mode_config(mode_name),
                )
            )
        return "\n\n".join(blocks)
