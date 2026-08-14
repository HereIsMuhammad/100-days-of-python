# Day 95: Code Quality (Linting & Formatting with Black/Ruff)

## Why Code Quality Tools?
As projects grow, consistent formatting and catching common mistakes
automatically saves huge amounts of time in code review and prevents bugs.

## Formatters vs Linters
- **Formatter** (e.g. `black`): automatically rewrites code to follow a
  consistent style (spacing, quotes, line length). No debate needed —
  it just formats.
- **Linter** (e.g. `ruff`, `flake8`, `pylint`): analyzes code for
  potential bugs, unused imports, style violations — without changing
  the code itself (usually).

## Black — The Uncompromising Formatter
```bash
pip install black
black my_script.py        # formats one file
black .                   # formats the whole project
black --check .           # check only, don't modify (good for CI)
```
Black has almost no configuration — that's the point. It ends
"tabs vs spaces"-style arguments on a team.

## Ruff — Extremely Fast Linter (and formatter)
```bash
pip install ruff
ruff check .               # lint the project
ruff check . --fix         # auto-fix what it safely can
ruff format .               # ruff can format too (Black-compatible)
```
Ruff is written in Rust and is dramatically faster than older linters
like `flake8` or `pylint`, while covering hundreds of the same checks.

## Example: Before and After
```python
# Before (messy)
def add(a,b):
    return a+b
x=[1,2,3]
import os
```
```python
# After `black` + `ruff --fix`
import os


def add(a, b):
    return a + b


x = [1, 2, 3]
```
(Ruff would also flag `import os` as unused if it's never referenced.)

## Configuring in `pyproject.toml`
```toml
[tool.black]
line-length = 88

[tool.ruff]
line-length = 88
select = ["E", "F", "I"]   # error, pyflakes, import-sorting rules
```

## Pre-commit Hooks (auto-run on every commit)
```bash
pip install pre-commit
```
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.1.1
    hooks:
      - id: black
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.0
    hooks:
      - id: ruff
```
```bash
pre-commit install
```
Now formatting/linting runs automatically before every `git commit`.

## Summary
`black` keeps formatting consistent without arguments; `ruff` quickly
catches bugs, unused code, and style issues. Together — often wired up
via pre-commit hooks — they keep a growing codebase clean with almost no
manual effort.
