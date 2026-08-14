# Day 100: Capstone Project — Release & Final Polish 🎉

## The Final Day!
100 days of consistent Python practice — from `print("Hello, World!")` on
Day 1 to a fully tested, authenticated REST API with a database backend
today. This final phase is about **polish and release**, the last step of
any real project.

## Final Polish Checklist
- [ ] **README**: clear project description, setup instructions, and
  example API calls (or a link to `/docs`).
- [ ] **Environment variables**: move secrets (like `SECRET_KEY`) out of
  source code into a `.env` file, loaded with `python-dotenv`.
- [ ] **Error handling**: confirm every route returns sensible status
  codes and error messages (Day 85).
- [ ] **Logging**: add basic logging (Day 74) instead of `print()` for
  debugging production issues.
- [ ] **CI pipeline**: confirm the GitHub Actions workflow (Day 96) runs
  tests automatically on every push.
- [ ] **requirements.txt / pyproject.toml**: pin dependencies (Day 94) so
  the project installs reproducibly.
- [ ] **Final test pass**: run the full suite (Day 99) once more before
  tagging a release.

## Using Environment Variables for Secrets
```bash
pip install python-dotenv
```
```python
# .env (never commit this file — add it to .gitignore)
SECRET_KEY=your-real-secret-key-here
DATABASE_URL=sqlite:///./production.db
```
```python
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
```

## Writing a Good README
A good README (recap of documentation habits from Day 1 onward) includes:
1. **What** the project does (one paragraph).
2. **How** to install and run it (exact commands).
3. **API overview** (endpoints table, or a link to `/docs`).
4. **How to run tests**.
5. **License** (this repo already uses MIT — Day 94 packaging touches on
   this too).

## Tagging a Release on GitHub
```bash
git tag -a v1.0.0 -m "Capstone v1.0.0 — Expense Tracker API"
git push origin v1.0.0
```
This creates a permanent, referenceable snapshot of the finished project.

## Reflecting on 100 Days
Over 100 days this journey covered:
- **Fundamentals** (Days 1-42): syntax, data types, control flow, functions.
- **OOP** (Days 43-56): classes, inheritance, polymorphism, data structures.
- **Intermediate Python** (Days 57-76): decorators, generators, async
  concepts, files, databases, concurrency.
- **Testing** (Days 78-79): unittest and pytest.
- **Web scraping** (Days 80-82).
- **Web APIs** (Days 83-89): HTTP, FastAPI, REST, JWT auth, SQLAlchemy.
- **Data tools** (Days 90-93): NumPy, Pandas, Matplotlib/Seaborn.
- **Professional practices** (Days 94-96): packaging, linting, CI/CD.
- **Capstone** (Days 97-100): a complete, tested, deployable project.

## What's Next?
- Deploy the API somewhere real (Railway, Render, Fly.io, or a VPS).
- Add a frontend (even a simple one) that consumes this API.
- Keep building — pick a new project and apply everything learned here.

## Summary
Day 100 isn't the end of learning Python — it's proof that consistent,
daily practice compounds into real, shippable skill. Congratulations on
finishing #100DaysOfPython! 🐍🎉
