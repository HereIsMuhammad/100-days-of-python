"""
Day 94: Python Packaging & Setup
This script generates a minimal, ready-to-use package skeleton
(with a pyproject.toml, package folder, and a starter test)
so you can see exactly what a packaged project looks like.
"""

import os

PROJECT_NAME = "day94_demo_package"

PYPROJECT_TOML = f'''[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "{PROJECT_NAME}"
version = "0.1.0"
description = "A demo package generated on Day 94 of #100DaysOfPython"
readme = "README.md"
requires-python = ">=3.9"
dependencies = []

[project.optional-dependencies]
dev = ["pytest"]
'''

INIT_PY = '''"""Day 94 demo package."""

from .core import greet

__all__ = ["greet"]
'''

CORE_PY = '''def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}! This package was built on Day 94."
'''

TEST_PY = f'''from {PROJECT_NAME}.core import greet


def test_greet():
    assert greet("Ali") == "Hello, Ali! This package was built on Day 94."
'''

README_MD = f"# {PROJECT_NAME}\n\nA minimal demo package generated for Day 94 (#100DaysOfPython).\n"


def scaffold_package(base_dir: str = "."):
    root = os.path.join(base_dir, PROJECT_NAME + "_project")
    pkg_dir = os.path.join(root, "src", PROJECT_NAME)
    tests_dir = os.path.join(root, "tests")

    os.makedirs(pkg_dir, exist_ok=True)
    os.makedirs(tests_dir, exist_ok=True)

    files = {
        os.path.join(root, "pyproject.toml"): PYPROJECT_TOML,
        os.path.join(root, "README.md"): README_MD,
        os.path.join(pkg_dir, "__init__.py"): INIT_PY,
        os.path.join(pkg_dir, "core.py"): CORE_PY,
        os.path.join(tests_dir, "test_core.py"): TEST_PY,
    }

    for path, content in files.items():
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Created: {path}")

    print(f"\nDone! Try:\n  cd {root}\n  pip install -e .\n  pytest")


if __name__ == "__main__":
    scaffold_package()
