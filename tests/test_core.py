"""Tests for matplotlib-dark core functionality"""

import pytest
import matplotlib.pyplot as plt
import matplotlib_dark as mdk


@pytest.fixture(autouse=True)
def restore_matplotlib_style():
    """Keep global Matplotlib state from leaking between tests."""
    original = plt.rcParams.copy()
    yield
    plt.rcParams.update(original)


def test_dark_mode_default():
    """Test applying default dark mode"""
    mdk.dark_mode()
    assert plt.rcParams['figure.facecolor'] == '#1e1e1e'
    mdk.light_mode()


def test_dark_mode_nord():
    """Test applying nord theme"""
    mdk.dark_mode(theme='nord')
    assert plt.rcParams['figure.facecolor'] == '#2E3440'
    mdk.light_mode()


def test_dark_mode_monokai():
    """Test applying monokai theme"""
    mdk.dark_mode(theme='monokai')
    assert plt.rcParams['figure.facecolor'] == '#272822'
    mdk.light_mode()


def test_dark_mode_dracula():
    """Test applying dracula theme"""
    mdk.dark_mode(theme='dracula')
    assert plt.rcParams['figure.facecolor'] == '#282A36'
    mdk.light_mode()


def test_invalid_theme():
    """Test that invalid theme raises ValueError"""
    with pytest.raises(ValueError):
        mdk.dark_mode(theme='nonexistent')


def test_light_mode_restore():
    """Test that light mode restores defaults"""
    original_bg = plt.rcParams['figure.facecolor']
    mdk.dark_mode()
    mdk.light_mode()
    assert plt.rcParams['figure.facecolor'] == original_bg


def test_get_available_themes():
    """Test getting available themes"""
    themes = mdk.get_available_themes()
    assert isinstance(themes, list)
    assert 'default' in themes
    assert 'nord' in themes
    assert 'monokai' in themes
    assert 'dracula' in themes
    assert 'neon' in themes
    assert 'material' in themes


def test_set_theme():
    """Test set_theme function"""
    mdk.set_theme('nord')
    assert plt.rcParams['figure.facecolor'] == '#2E3440'
    mdk.light_mode()


def test_switching_theme_still_restores_original_style():
    original_bg = plt.rcParams['figure.facecolor']
    mdk.dark_mode('nord')
    mdk.dark_mode('dracula')
    mdk.light_mode()
    assert plt.rcParams['figure.facecolor'] == original_bg


def test_dark_theme_context_restores_style():
    original_bg = plt.rcParams['figure.facecolor']
    with mdk.dark_theme('material'):
        assert plt.rcParams['figure.facecolor'] == '#212121'
    assert plt.rcParams['figure.facecolor'] == original_bg


def test_dark_theme_context_restores_style_after_error():
    original_bg = plt.rcParams['figure.facecolor']
    with pytest.raises(RuntimeError):
        with mdk.dark_theme('neon'):
            raise RuntimeError('plot failed')
    assert plt.rcParams['figure.facecolor'] == original_bg
