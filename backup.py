#!/usr/bin/env python3
import shutil
from pathlib import Path

repo_dir = Path(__file__).parent.resolve()
home = Path.home()

files_to_backup = [
    home / ".bashrc",
    home / ".config/waybar",
    home / ".config/hypr",
    home / ".config/hyprpaper",
    home / ".config/VSCodium/User/settings.json",
]

for path in files_to_backup:
    if path.exists():
        rel_path = path.relative_to(home)
        dest_path = repo_dir / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        if path.is_dir():
            shutil.copytree(path, dest_path, dirs_exist_ok=True)
        else:
            shutil.copy2(path, dest_path)
        print(f"Backed up {path} -> {dest_path}")
    else:
        print(f"Warning: {path} does not exist, skipping.")

print("\nBackup completed! Files saved at repo root, mimicking system structure.")
