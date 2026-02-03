"""Core functionality for matplotlib-dark"""

import matplotlib.pyplot as plt
from matplotlib import cycler
from .themes import THEMES

# Store original rcParams
_original_params = None


def dark_mode(theme='default'):
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


def light_mode():
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
        plt.rcdefaults()
    else:
        plt.rcParams.update(_original_params)
        _original_params = None


def set_theme(theme_name):
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
        _original_params = plt.rcParams.copy()
    
    theme = THEMES[theme_name]
    
    # Apply theme colors
    plt.rcParams.update({
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
    plt.rcParams['axes.prop_cycle'] = cycler(color=colors)


def get_available_themes():
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
