"""
matplotlib-dark: matplotlib, but in dark mode
A lightweight package to apply dark themes to matplotlib plots.
"""

__version__ = "0.1.0"
__author__ = "Eduardo J. Barrios"

from .core import dark_mode, light_mode, set_theme, get_available_themes
from .themes import THEMES

__all__ = [
    "dark_mode",
    "light_mode", 
    "set_theme",
    "get_available_themes",
    "THEMES",
]
