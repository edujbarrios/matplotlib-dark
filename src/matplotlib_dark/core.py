"""Core functionality for matplotlib-dark."""

from contextlib import contextmanager
from typing import Iterator, List, Optional

import matplotlib as mpl
from matplotlib import cycler

from .themes import THEMES

# Store original rcParams
_original_params: Optional[dict] = None


def dark_mode(theme: str = "default") -> None:
    """
    Apply a dark theme to matplotlib plots.
    
    Parameters
    ----------
    theme : str, optional
        The name of the theme to apply. Available themes: 
        'default', 'nord', 'monokai', 'dracula'
        Default is 'default'.
    
    Examples
    --------
    >>> import matplotlib_dark as mdk
    >>> mdk.dark_mode()
    >>> mdk.dark_mode(theme='nord')
    """
    set_theme(theme)


def light_mode() -> None:
    """
    Restore matplotlib to its default light theme.
    
    Examples
    --------
    >>> import matplotlib_dark as mdk
    >>> mdk.dark_mode()
    >>> # ... create plots ...
    >>> mdk.light_mode()  # Restore defaults
    """
    global _original_params
    
    if _original_params is None:
        mpl.rcdefaults()
    else:
        mpl.rcParams.update(_original_params)
        _original_params = None


def set_theme(theme_name: str) -> None:
    """
    Set a specific dark theme.
    
    Parameters
    ----------
    theme_name : str
        The name of the theme to apply.
        
    Raises
    ------
    ValueError
        If the theme name is not recognized.
    """
    global _original_params
    
    if theme_name not in THEMES:
        available = ', '.join(THEMES.keys())
        raise ValueError(
            f"Unknown theme '{theme_name}'. "
            f"Available themes: {available}"
        )
    
    # Save original params on first call
    if _original_params is None:
        _original_params = dict(mpl.rcParams)
    
    theme = THEMES[theme_name]
    
    # Apply theme colors
    mpl.rcParams.update({
        'figure.facecolor': theme['bg_color'],
        'axes.facecolor': theme['axes_bg'],
        'axes.edgecolor': theme['text_color'],
        'axes.labelcolor': theme['text_color'],
        'axes.grid': True,
        'grid.color': theme['grid_color'],
        'grid.alpha': 0.3,
        'text.color': theme['text_color'],
        'xtick.color': theme['text_color'],
        'ytick.color': theme['text_color'],
        'legend.facecolor': theme['axes_bg'],
        'legend.edgecolor': theme['grid_color'],
        'savefig.facecolor': theme['bg_color'],
        'savefig.edgecolor': theme['bg_color'],
    })
    
    # Set color cycle
    colors = theme.get('colors', [
        '#8FBCBB', '#88C0D0', '#81A1C1', '#5E81AC',
        '#BF616A', '#D08770', '#EBCB8B', '#A3BE8C', '#B48EAD'
    ])
    mpl.rcParams['axes.prop_cycle'] = cycler(color=colors)


def get_available_themes() -> List[str]:
    """
    Get a list of available theme names.
    
    Returns
    -------
    list
        List of available theme names.
    
    Examples
    --------
    >>> import matplotlib_dark as mdk
    >>> themes = mdk.get_available_themes()
    >>> print(themes)
    ['default', 'nord', 'monokai', 'dracula']
    """
    return list(THEMES.keys())


@contextmanager
def dark_theme(theme: str = "default") -> Iterator[None]:
    """Temporarily apply a dark theme and restore the current style afterwards.

    This is safe to nest and is useful when only one plot should use the theme.

    Examples
    --------
    >>> import matplotlib_dark as mdk
    >>> with mdk.dark_theme("nord"):
    ...     pass  # Create and save a plot here.
    """
    global _original_params
    previous_original = _original_params
    with mpl.rc_context():
        set_theme(theme)
        try:
            yield
        finally:
            _original_params = previous_original
