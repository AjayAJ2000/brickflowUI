"""Compatibility wrapper so the published distribution can support `import bricksflowui`."""

import brickflowui as _brickflowui
from brickflowui import *  # noqa: F401,F403

__version__ = _brickflowui.__version__
