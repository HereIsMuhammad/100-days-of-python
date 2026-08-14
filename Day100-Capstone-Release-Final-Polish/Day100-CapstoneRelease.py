"""
Day 100: Capstone Project — Release & Final Polish
Final release-readiness checker for the Expense Tracker capstone project.
Scans the project folder and reports what's in place vs still missing
before calling it "v1.0.0 ready".
"""

import os


CHECKLIST = {
    "README.md": "Project documentation",
    "pyproject.toml": "Packaging & dependency definition (Day 94)",
    ".github/workflows/tests.yml": "CI pipeline (Day 96)",
    ".env": "Environment variables for secrets (should exist locally, NOT committed)",
    ".gitignore": "Ignore rules (should include .env, __pycache__, *.db)",
    "tests": "Test suite folder (Day 99)",
    "LICENSE": "Project license",
}


def check_release_readiness(project_root: str = "."):
    print(f"Checking release readiness for: {os.path.abspath(project_root)}\n")

    results = {}
    for path, description in CHECKLIST.items():
        full_path = os.path.join(project_root, path)
        exists = os.path.exists(full_path)
        results[path] = exists
        status = "✅ Found" if exists else "❌ Missing"
        print(f"{status:12} {path:35} — {description}")

    total = len(CHECKLIST)
    found = sum(results.values())
    print(f"\nReadiness: {found}/{total} checks passed")

    if found == total:
        print("🎉 Project looks release-ready! Consider tagging v1.0.0:")
        print("   git tag -a v1.0.0 -m 'Capstone v1.0.0 — Expense Tracker API'")
        print("   git push origin v1.0.0")
    else:
        missing = [k for k, v in results.items() if not v]
        print("Still missing:", ", ".join(missing))

    return results


def print_completion_banner():
    banner = r"""
    ============================================
       100 DAYS OF PYTHON — COMPLETE! 🎉🐍
    ============================================
    Day 1:   print("Hello, World!")
    Day 100: A tested, authenticated REST API
    ============================================
    """
    print(banner)


if __name__ == "__main__":
    check_release_readiness()
    print_completion_banner()
