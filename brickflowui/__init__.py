"""
BrickflowUI — Databricks-first, React-style Python UI library.

Usage:
    import brickflowui as db

    app = db.App()

    @app.page("/", title="Home", icon="Home")
    def home_page():
        count, set_count = db.use_state(0)
        return db.Column([
            db.Text("My App", variant="h1"),
            db.Text(f"Count: {count}"),
            db.Button("Increment", on_click=lambda: set_count(count + 1)),
        ])

    if __name__ == "__main__":
        app.run()
"""

from .app import App
from .auth import (
    HeaderAuthProvider,
    Principal,
    StaticAuthProvider,
    current_app_identity,
    current_principal,
    current_user,
    is_authenticated,
    require_auth,
    require_role,
)
from .state import use_state, use_effect, use_memo, use_context, set_context
from .components import (
    # Layout
    Column,
    Row,
    Card,
    Grid,
    Divider,
    Spacer,
    # Typography
    Text,
    Code,
    # Interactive controls
    Button,
    Input,
    Select,
    Checkbox,
    Toggle,
    Slider,
    # Data display
    Table,
    Badge,
    Alert,
    Spinner,
    Progress,
    Stat,
    # Navigation & structure
    Tabs,
    TabItem,
    Sidebar,
    NavItem,
    Modal,
    # Charts/visualization
    Plot,
    AreaChart,
    BarChart,
    LineChart,
    DonutChart,
    # Forms
    Form,
    # Databricks-specific
    CatalogBrowser,
    WarehouseSelector,
    JobTrigger,
)

__version__ = "0.1.0"
__all__ = [
    # Core
    "App",
    "Principal",
    "HeaderAuthProvider",
    "StaticAuthProvider",
    # Hooks
    "use_state",
    "use_effect",
    "use_memo",
    "use_context",
    "set_context",
    "current_principal",
    "current_user",
    "current_app_identity",
    "is_authenticated",
    "require_auth",
    "require_role",
    # Layout
    "Column",
    "Row",
    "Card",
    "Grid",
    "Divider",
    "Spacer",
    # Typography
    "Text",
    "Code",
    # Controls
    "Button",
    "Input",
    "Select",
    "Checkbox",
    "Toggle",
    "Slider",
    # Data display
    "Table",
    "Badge",
    "Alert",
    "Spinner",
    "Progress",
    "Stat",
    # Navigation
    "Tabs",
    "TabItem",
    "Sidebar",
    "NavItem",
    "Modal",
    # Visualization
    "Plot",
    "AreaChart",
    "BarChart",
    "LineChart",
    "DonutChart",
    # Forms
    "Form",
    # Databricks
    "CatalogBrowser",
    "WarehouseSelector",
    "JobTrigger",
]
