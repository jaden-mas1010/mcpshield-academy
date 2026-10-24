"""Local-only test runner. Never expose this subprocess to the dashboard API."""
import argparse
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a student's coding-mission security tests locally")
    parser.add_argument("--mission", type=int, choices=range(1, 6), help="Mission number 1–5 (default: all)")
    args = parser.parse_args()
    target = (f"code_lab/tests/test_mission{args.mission:02}.py" if args.mission else "code_lab/tests")
    print(f"Checking: {target}", flush=True)
    cmd = [sys.executable, "-m", "pytest", target, "-v", "--import-mode=importlib"]
    return subprocess.call(cmd, cwd=BASE)


if __name__ == "__main__":
    raise SystemExit(main())
