import brickflowui
import bricksflowui


def test_package_alias_exposes_app():
    assert brickflowui.App is bricksflowui.App


def test_package_alias_exposes_version():
    assert bricksflowui.__version__ == brickflowui.__version__
