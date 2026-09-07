<div align="center">

# matplotlib-dark

**Automatic dark mode for Matplotlib — polished charts without designing a theme.**

[![CI](https://github.com/edujbarrios/matplotlib-dark/actions/workflows/ci.yml/badge.svg)](https://github.com/edujbarrios/matplotlib-dark/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/matplotlib-dark.svg?logo=pypi&logoColor=white&cacheSeconds=300)](https://pypi.org/project/matplotlib-dark/)
[![Python](https://img.shields.io/pypi/pyversions/matplotlib-dark)](https://pypi.org/project/matplotlib-dark/)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

</div>

`matplotlib-dark` is the automatic alternative to hand-picking backgrounds,
grid colors, text contrast, and line palettes for every chart. Activate it in
one line, then keep using the Matplotlib API you already know.

![Six matplotlib-dark themes compared](https://raw.githubusercontent.com/edujbarrios/matplotlib-dark/main/images/theme_comparison.png)

## Installation

```bash
python -m pip install matplotlib-dark
```

Python 3.9+ and Matplotlib 3.5+ are supported.

## Quick start

```python
import matplotlib.pyplot as plt
import matplotlib_dark as mdk

mdk.dark_mode()  # That's it: every following chart uses dark mode.

plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.title("Ready for the dark")
plt.show()
```

No custom CSS, manual color selection, or complex design code is required.

## Choose a theme

```python
mdk.dark_mode("nord")
```

Six ready-to-use themes are included: `default`, `nord`, `monokai`,
`dracula`, `neon`, and `material`.

```python
print(mdk.get_available_themes())
```

## Apply dark mode temporarily

Use the context manager when only some charts should be dark. Your previous
Matplotlib configuration is restored automatically, even if plotting fails.

```python
with mdk.dark_theme("dracula"):
    plt.plot([1, 2, 3], [3, 1, 4])
    plt.savefig("dark-chart.png")
```

For global mode, restore your original configuration explicitly:

```python
mdk.dark_mode("material")
# Create charts...
mdk.light_mode()
```

## Why matplotlib-dark?

- One-line automatic dark mode
- Six coordinated color palettes
- Works with the complete Matplotlib API
- Global mode or safe, temporary context manager
- Dark backgrounds are preserved when saving figures
- Zero dependencies beyond Matplotlib

## Development

```bash
git clone https://github.com/edujbarrios/matplotlib-dark.git
cd matplotlib-dark
python -m pip install -e ".[dev]"
python -m pytest
python -m build
python -m twine check dist/*
```

## License

MIT © Eduardo J. Barrios
