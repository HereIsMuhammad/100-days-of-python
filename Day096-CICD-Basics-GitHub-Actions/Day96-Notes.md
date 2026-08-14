# Day 96: CI/CD Basics with GitHub Actions

## What is CI/CD?
- **CI (Continuous Integration)**: automatically build & test your code
  every time you push changes, catching bugs early.
- **CD (Continuous Delivery/Deployment)**: automatically package and
  deploy your code once it passes CI.

## GitHub Actions Basics
GitHub Actions runs "workflows" defined in YAML files inside
`.github/workflows/`. Each workflow is triggered by events (push, pull
request, schedule, etc.) and runs one or more **jobs**, each made of
**steps**.

## A Basic Workflow: Run Tests on Every Push
```yaml
# .github/workflows/tests.yml
name: Run Tests

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest

      - name: Run tests
        run: pytest
```

## Testing Across Multiple Python Versions (matrix)
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.9", "3.10", "3.11", "3.12"]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: ${{ matrix.python-version }}
      - run: pip install -r requirements.txt pytest
      - run: pytest
```

## Adding Linting to the Pipeline
```yaml
      - name: Lint with ruff
        run: |
          pip install ruff
          ruff check .
      - name: Check formatting with black
        run: |
          pip install black
          black --check .
```

## Deploying on Success (CD example)
```yaml
  deploy:
    needs: test              # only runs if the `test` job succeeds
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy
        run: echo "Deploying application..."
```

## Key Concepts Recap
| Term | Meaning |
|---|---|
| Workflow | A YAML file defining automated steps |
| Trigger (`on:`) | Event that starts the workflow (push, PR, schedule) |
| Job | A set of steps that run on a single machine (runner) |
| Step | A single command or reusable action |
| Runner | The virtual machine executing the job (e.g. `ubuntu-latest`) |

## Summary
CI/CD pipelines automatically test (and optionally deploy) your code on
every push, catching bugs before they reach production and removing
manual, error-prone release steps.
