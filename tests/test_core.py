"""Tests for matplotlib-dark core functionality"""

import pytest
import matplotlib.pyplot as plt
import matplotlib_dark as mdk


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


def test_set_theme():
    """Test set_theme function"""
    mdk.set_theme('nord')
    assert plt.rcParams['figure.facecolor'] == '#2E3440'
    mdk.light_mode()
