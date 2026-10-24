"""Restore one coding exercise; back up the student's current file first."""
import argparse
from datetime import datetime
from pathlib import Path
import shutil

BASE = Path(__file__).resolve().parent


def reset_mission(number: int) -> Path:
    if type(number) is not int or number not in range(1, 6):
        raise ValueError("Mission must be 1 to 5")
    src = BASE / "starters" / f"mission{number:02}.py"
    dest = BASE / "challenges" / f"mission{number:02}.py"
    backup_dir = BASE.parent / ".lab-backups" / "coding"
    if not src.is_file():
        raise FileNotFoundError(src)
    if dest.is_file():
        backup_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        backup = backup_dir / f"mission{number:02}_{timestamp}.py"
        shutil.copy2(dest, backup)
    else:
        backup = None
    shutil.copyfile(src, dest)
    return backup


def main():
    parser = argparse.ArgumentParser(description="Back up and reset a local coding mission")
    parser.add_argument("--mission", type=int, required=True, choices=range(1, 6))
    parser.add_argument("--yes", action="store_true", help="Confirm replacement")
    args = parser.parse_args()
    if not args.yes:
        parser.error("Add --yes to confirm replacing the current challenge code")
    saved = reset_mission(args.mission)
    print(f"Mission {args.mission:02} reset to insecure starter.")
    if saved:
        print(f"Your previous code was backed up to: {saved}")


if __name__ == "__main__":
    main()
