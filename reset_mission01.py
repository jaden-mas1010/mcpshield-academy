"""Make backup, restore Mission 01 intentionally vulnerable starter code."""
from pathlib import Path
from datetime import datetime
import shutil
import sys

BASE = Path(__file__).resolve().parent
STARTER = BASE / 'starter' / 'mission01.py.template'
TARGET = BASE / 'missions' / 'mission01.py'
BACKUP_DIR = BASE / '.lab-backups'


def reset_mission(template_path: Path, target_path: Path, backup_dir: Path):
    if not template_path.is_file():
        raise FileNotFoundError('Starter template not found')
    backup_path = None
    if target_path.exists():
        backup_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
        backup_path = backup_dir / f'mission01_{timestamp}.py'
        shutil.copy2(target_path, backup_path)
    shutil.copyfile(template_path, target_path)
    return backup_path

if __name__ == '__main__':
    if sys.argv[1:] != ['--reset']:
        print('Usage: python reset_mission01.py --reset')
        raise SystemExit(2)
    saved = reset_mission(STARTER, TARGET, BACKUP_DIR)
    print('Mission 01 reset. Saved previous work:', saved)
    print('Restart MCP server to load the reset policy.')
