"""
BrickflowUI primitive components.

Each function returns a VNode. Think of these as your JSX — but pure Python.
Usage:
    from brickflowui import components as ui
    node = ui.Column([ui.Text("Hello!"), ui.Button("Click me", on_click=handler)])
"""

from __future__ import annotations

from contextlib import contextmanager
from typing import Any, Callable, Dict, Iterator, List, Optional, Literal

from .vdom import VNode, EventHandler

# ── Type aliases ────────────────────────────────────────────────────────────

ButtonVariant = Literal["primary", "secondary", "danger", "ghost", "outline"]
AlertType = Literal["info", "success", "warning", "error"]
TextVariant = Literal["h1", "h2", "h3", "h4", "body", "caption", "code", "label"]
InputType = Literal["text", "password", "email", "number", "url", "search", "date", "textarea"]
BadgeColor = Literal["blue", "green", "yellow", "red", "purple", "gray", "orange"]


# ── Layout ───────────────────────────────────────────────────────────────────


def Column(
    children: List[VNode],
    gap: int = 2,
    padding: int = 0,
    align: Literal["start", "center", "end", "stretch"] = "stretch",
    **kwargs,
) -> VNode:
    """Vertical stack of children."""
    props = {"gap": gap, "padding": padding, "align": align, **kwargs}
    return VNode(
        type="Column",
        props=props,
        children=children,
    )


def Row(
    children: List[VNode],
    gap: int = 2,
    wrap: bool = False,
    align: Literal["start", "center", "end", "stretch"] = "center",
    justify: Literal["start", "center", "end", "between", "around"] = "start",
    **kwargs,
) -> VNode:
    """Horizontal row of children."""
    return VNode(
        type="Row",
        props={"gap": gap, "wrap": wrap, "align": align, "justify": justify, **kwargs},
        children=children,
    )


def Card(
    children: List[VNode],
    title: Optional[str] = None,
    subtitle: Optional[str] = None,
    bordered: bool = True,
    padding: int = 4,
    hover: bool = False,
    **kwargs,
) -> VNode:
    """A surface card container."""
    return VNode(
        type="Card",
        props={"title": title, "subtitle": subtitle, "bordered": bordered, "padding": padding, "hover": hover, **kwargs},
        children=children,
    )


def Grid(
    children: List[VNode],
    cols: int = 2,
    gap: int = 4,
) -> VNode:
    """Responsive grid layout."""
    return VNode(
        type="Grid",
        props={"cols": cols, "gap": gap, "style": {"--cols": str(cols)}},
        children=children,
    )


def Divider(label: Optional[str] = None) -> VNode:
    """Horizontal rule, optionally with a label."""
    return VNode(type="Divider", props={"label": label})


def Spacer(size: int = 4) -> VNode:
    """Blank vertical spacer."""
    return VNode(type="Spacer", props={"size": size})


# ── Typography ────────────────────────────────────────────────────────────────


def Text(
    value: str,
    variant: TextVariant = "body",
    color: Optional[str] = None,
    bold: bool = False,
    italic: bool = False,
    muted: bool = False,
) -> VNode:
    """A text/heading element."""
    return VNode(
        type="Text",
        props={"value": value, "variant": variant, "color": color, "bold": bold, "italic": italic, "muted": muted},
    )


def Code(value: str, language: str = "python") -> VNode:
    """Syntax-highlighted code block."""
    return VNode(type="Code", props={"value": value, "language": language})


# ── Interactive Controls ───────────────────────────────────────────────────


def Button(
    label: str,
    on_click: Optional[EventHandler] = None,
    variant: ButtonVariant = "primary",
    icon: Optional[str] = None,
    disabled: bool = False,
    loading: bool = False,
    html_type: Literal["button", "submit", "reset"] = "button",
    **kwargs,
) -> VNode:
    handlers: Dict[str, EventHandler] = {}
    if on_click:
        handlers["click"] = on_click
    return VNode(
        type="Button",
        props={"label": label, "variant": variant, "icon": icon, "disabled": disabled, "loading": loading, "htmlType": html_type, **kwargs},
        event_handlers=handlers,
    )


def Input(
    name: str,
    label: Optional[str] = None,
    type: InputType = "text",
    placeholder: str = "",
    value: str = "",
    on_change: Optional[Callable[[str], None]] = None,
    disabled: bool = False,
    required: bool = False,
    error: Optional[str] = None,
) -> VNode:
    handlers: Dict[str, EventHandler] = {}
    if on_change:
        handlers["change"] = on_change
    return VNode(
        type="Input",
        props={"name": name, "label": label, "inputType": type, "placeholder": placeholder,
               "value": value, "disabled": disabled, "required": required, "error": error},
        event_handlers=handlers,
    )


def Select(
    name: str,
    options: List[Dict[str, str]],
    label: Optional[str] = None,
    value: Optional[str] = None,
    placeholder: str = "Select an option",
    on_change: Optional[Callable[[str], None]] = None,
    disabled: bool = False,
) -> VNode:
    """Dropdown select. options = [{"label": "...", "value": "..."}]"""
    handlers: Dict[str, EventHandler] = {}
    if on_change:
        handlers["change"] = on_change
    return VNode(
        type="Select",
        props={"name": name, "options": options, "label": label, "value": value,
               "placeholder": placeholder, "disabled": disabled},
        event_handlers=handlers,
    )


def Checkbox(
    name: str,
    label: str,
    checked: bool = False,
    on_change: Optional[Callable[[bool], None]] = None,
    disabled: bool = False,
) -> VNode:
    handlers: Dict[str, EventHandler] = {}
    if on_change:
        handlers["change"] = on_change
    return VNode(
        type="Checkbox",
        props={"name": name, "label": label, "checked": checked, "disabled": disabled},
        event_handlers=handlers,
    )


def Toggle(
    name: str,
    label: str,
    checked: bool = False,
    on_change: Optional[Callable[[bool], None]] = None,
    disabled: bool = False,
) -> VNode:
    handlers: Dict[str, EventHandler] = {}
    if on_change:
        handlers["change"] = on_change
    return VNode(
        type="Toggle",
        props={"name": name, "label": label, "checked": checked, "disabled": disabled},
        event_handlers=handlers,
    )


def Slider(
    name: str,
    label: Optional[str] = None,
    min: float = 0,
    max: float = 100,
    step: float = 1,
    value: float = 0,
    on_change: Optional[Callable[[float], None]] = None,
) -> VNode:
    handlers: Dict[str, EventHandler] = {}
    if on_change:
        handlers["change"] = on_change
    return VNode(
        type="Slider",
        props={"name": name, "label": label, "min": min, "max": max, "step": step, "value": value},
        event_handlers=handlers,
    )


# ── Data Display ───────────────────────────────────────────────────────────


def Table(
    data: List[Dict[str, Any]],
    columns: Optional[List[Dict[str, Any]]] = None,
    pagination: int = 20,
    on_row_click: Optional[Callable[[Dict[str, Any]], None]] = None,
    editable: bool = False,
    loading: bool = False,
    empty_message: str = "No data available",
) -> VNode:
    """
    Data table. columns = [{"key": "col", "label": "Column", "sortable": True}]
    If columns is None, keys are auto-inferred from data[0].
    """
    if columns is None and data:
        columns = [{"key": k, "label": k.replace("_", " ").title(), "sortable": True} for k in data[0].keys()]
    handlers: Dict[str, EventHandler] = {}
    if on_row_click:
        handlers["rowClick"] = on_row_click
    return VNode(
        type="Table",
        props={"data": data, "columns": columns or [], "pagination": pagination,
               "editable": editable, "loading": loading, "emptyMessage": empty_message},
        event_handlers=handlers,
    )


def Badge(label: str, color: BadgeColor = "blue") -> VNode:
    return VNode(type="Badge", props={"label": label, "color": color})


def Alert(
    message: str,
    type: AlertType = "info",
    title: Optional[str] = None,
    dismissible: bool = False,
) -> VNode:
    return VNode(
        type="Alert",
        props={"message": message, "alertType": type, "title": title, "dismissible": dismissible},
    )


def Spinner(size: Literal["sm", "md", "lg"] = "md") -> VNode:
    return VNode(type="Spinner", props={"size": size})


def Progress(value: float, max: float = 100, label: Optional[str] = None, color: str = "blue") -> VNode:
    """Progress bar. value and max are numbers."""
    return VNode(type="Progress", props={"value": value, "max": max, "label": label, "color": color})


def Stat(
    label: str,
    value: str,
    delta: Optional[str] = None,
    delta_type: Literal["increase", "decrease", "neutral"] = "neutral",
    icon: Optional[str] = None,
) -> VNode:
    """KPI stat card (number + label + optional delta)."""
    return VNode(
        type="Stat",
        props={"label": label, "value": value, "delta": delta, "deltaType": delta_type, "icon": icon},
    )


# ── Navigation & Structure ─────────────────────────────────────────────────


def Tabs(
    items: List[VNode],
    default_active: int = 0,
    on_change: Optional[Callable[[int], None]] = None,
) -> VNode:
    """Tab container. Children should be TabItem nodes."""
    handlers: Dict[str, EventHandler] = {}
    if on_change:
        handlers["change"] = on_change
    return VNode(
        type="Tabs",
        props={"defaultActive": default_active},
        children=items,
        event_handlers=handlers,
    )


def TabItem(label: str, children: List[VNode], icon: Optional[str] = None) -> VNode:
    return VNode(type="TabItem", props={"label": label, "icon": icon}, children=children)


def Sidebar(
    items: List[VNode],
    logo: Optional[str] = None,
    brand_name: str = "BrickflowUI",
    collapsed: bool = False,
    **kwargs,
) -> VNode:
    return VNode(
        type="Sidebar",
        props={"logo": logo, "brandName": brand_name, "collapsed": collapsed, **kwargs},
        children=items,
    )


def NavItem(
    label: str,
    path: str,
    icon: Optional[str] = None,
    badge: Optional[str] = None,
) -> VNode:
    return VNode(type="NavItem", props={"label": label, "path": path, "icon": icon, "badge": badge})


def Modal(
    visible: bool,
    title: str,
    children: List[VNode],
    on_close: Optional[EventHandler] = None,
    size: Literal["sm", "md", "lg", "xl"] = "md",
) -> VNode:
    handlers: Dict[str, EventHandler] = {}
    if on_close:
        handlers["close"] = on_close
    return VNode(
        type="Modal",
        props={"visible": visible, "title": title, "size": size},
        children=children,
        event_handlers=handlers,
    )


# ── Data Visualization ──────────────────────────────────────────────────────


def Plot(figure: Dict[str, Any]) -> VNode:
    """Renders a Plotly figure dict. Pass the result of plotly.graph_objects.Figure."""
    # Support both dict and plotly Figure objects
    if hasattr(figure, "to_json"):
        import json
        figure = json.loads(figure.to_json())  # type: ignore
    return VNode(type="Plot", props={"figure": figure})


def AreaChart(
    data: List[Dict[str, Any]],
    x_key: str,
    y_keys: List[str],
    title: Optional[str] = None,
    colors: Optional[List[str]] = None,
    height: int = 300,
) -> VNode:
    return VNode(type="AreaChart", props={"data": data, "xKey": x_key, "yKeys": y_keys, "title": title, "colors": colors, "height": height})


def BarChart(
    data: List[Dict[str, Any]],
    x_key: str,
    y_keys: List[str],
    title: Optional[str] = None,
    colors: Optional[List[str]] = None,
    horizontal: bool = False,
    height: int = 300,
) -> VNode:
    return VNode(type="BarChart", props={"data": data, "xKey": x_key, "yKeys": y_keys, "title": title, "colors": colors, "horizontal": horizontal, "height": height})


def LineChart(
    data: List[Dict[str, Any]],
    x_key: str,
    y_keys: List[str],
    title: Optional[str] = None,
    colors: Optional[List[str]] = None,
    height: int = 300,
) -> VNode:
    return VNode(type="LineChart", props={"data": data, "xKey": x_key, "yKeys": y_keys, "title": title, "colors": colors, "height": height})


def DonutChart(
    data: List[Dict[str, str | float]],
    value_key: str = "value",
    label_key: str = "label",
    title: Optional[str] = None,
    height: int = 300,
) -> VNode:
    return VNode(type="DonutChart", props={"data": data, "valueKey": value_key, "labelKey": label_key, "title": title, "height": height})


# ── Forms ────────────────────────────────────────────────────────────────────


@contextmanager
def form(
    action: str,
    method: str = "POST",
    success_redirect: Optional[str] = None,
) -> Iterator[List[VNode]]:
    """
    Context manager that collects children and returns a Form VNode.

    Usage:
        with db.form("/api/submit", success_redirect="/dashboard") as f:
            f.append(db.Input(name="username", label="Username"))
            f.append(db.Button("Submit", html_type="submit"))
    """
    children: List[VNode] = []
    yield children
    # After context exits, return a Form VNode — but since we can't 'return' from a
    # context manager in Python, the form() must be assigned like a regular function.
    # Users should call form_node() below for more natural usage.


def Form(
    children: List[VNode],
    action: str,
    method: str = "POST",
    success_redirect: Optional[str] = None,
    reload_on_success: bool = False,
) -> VNode:
    """
    Wraps children in a form that posts JSON to `action`.
    Input/Select/Checkbox/Toggle components with `name` prop are serialized.
    """
    return VNode(
        type="Form",
        props={
            "action": action,
            "method": method,
            "successRedirect": success_redirect,
            "reloadOnSuccess": reload_on_success,
        },
        children=children,
    )


# ── Databricks-specific components ────────────────────────────────────────


def CatalogBrowser(
    on_select: Optional[Callable[[Dict[str, str]], None]] = None,
    selected: Optional[Dict[str, str]] = None,
) -> VNode:
    """
    Three-level catalog/schema/table browser backed by Unity Catalog REST API.
    on_select called with {"catalog": "...", "schema": "...", "table": "..."}
    """
    handlers: Dict[str, EventHandler] = {}
    if on_select:
        handlers["select"] = on_select
    return VNode(
        type="CatalogBrowser",
        props={"selected": selected or {}},
        event_handlers=handlers,
    )


def WarehouseSelector(
    on_select: Optional[Callable[[str], None]] = None,
    selected_id: Optional[str] = None,
    label: str = "SQL Warehouse",
) -> VNode:
    """Dropdown listing available SQL warehouses the current principal can use."""
    handlers: Dict[str, EventHandler] = {}
    if on_select:
        handlers["select"] = on_select
    return VNode(
        type="WarehouseSelector",
        props={"selectedId": selected_id, "label": label},
        event_handlers=handlers,
    )


def JobTrigger(
    job_id: str,
    label: str = "Run Job",
    on_complete: Optional[Callable[[Dict[str, Any]], None]] = None,
) -> VNode:
    """Button that triggers a Databricks Job run and shows status."""
    handlers: Dict[str, EventHandler] = {}
    if on_complete:
        handlers["complete"] = on_complete
    return VNode(
        type="JobTrigger",
        props={"jobId": job_id, "label": label},
        event_handlers=handlers,
    )
