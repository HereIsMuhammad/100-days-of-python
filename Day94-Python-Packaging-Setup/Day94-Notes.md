# Day 94: Python Packaging & Setup

## Why Package Your Code?
Turning a folder of scripts into an installable **package** lets others
(`pip install your-package`) — or your own future projects — reuse your
code cleanly, with proper dependency management and versioning.

## Modern Project Structure
```
my_package/
├── src/
│   └── my_package/
│       ├── __init__.py
│       ├── core.py
│       └── utils.py
├── tests/
│   └── test_core.py
├── pyproject.toml
├── README.md
└── LICENSE
```
The `src/` layout (code inside a `src/` folder) is the modern recommended
approach — it prevents accidentally importing your local uninstalled code
instead of the installed package during testing.

## `pyproject.toml` (modern standard, replaces `setup.py`)
```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "my_package"
version = "0.1.0"
description = "A short description of my package"
readme = "README.md"
requires-python = ">=3.9"
dependencies = [
    "requests>=2.28",
]

[project.optional-dependencies]
dev = ["pytest", "black", "ruff"]
```

## Installing Locally in "Editable" Mode
While developing, install your package so changes are picked up instantly:
```bash
pip install -e .
```

## Building & Publishing
```bash
pip install build twine
python -m build              # creates dist/*.whl and dist/*.tar.gz
twine upload dist/*          # publish to PyPI (needs a PyPI account)
```

## Virtual Environments (recap from Day 73)
Always develop inside a virtual environment to isolate dependencies:
```bash
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
```

## `requirements.txt` vs `pyproject.toml`
| | requirements.txt | pyproject.toml |
|---|---|---|
| Purpose | Pin exact deps for an app | Define a reusable, installable package |
| Use case | Deploying an application | Publishing a library |

## Summary
`pyproject.toml` is the modern standard for defining a Python package's
metadata, dependencies, and build system — replacing the older
`setup.py`/`setup.cfg` approach.
