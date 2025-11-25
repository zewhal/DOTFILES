#!/usr/bin/env python3
import subprocess
from pathlib import Path
import shutil

repo_dir = Path(__file__).parent.resolve()
home = Path.home()

packages = ["git", "base-devel", "vscodium", "waybar", "hyprland", "hyprpaper"]

def install_packages():
    print("Installing required packages...")
    try:
        subprocess.run(["sudo", "pacman", "-Syu", "--needed", *packages], check=True)
    except subprocess.CalledProcessError:
        print("Error installing packages. Make sure you have sudo rights.")

def restore_files():
    for src_path in repo_dir.rglob("*"):
        if src_path.name in ["backup.py", "install.py"]:
            continue
        rel_path = src_path.relative_to(repo_dir)
        dest_path = home / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        if src_path.is_dir():
            shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
        else:
            shutil.copy2(src_path, dest_path)
        print(f"Restored {src_path} -> {dest_path}")

if __name__ == "__main__":
    install_packages()
    restore_files()
    print("\nRestore completed! Your system structure has been restored from repo.")
