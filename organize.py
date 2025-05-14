#!/usr/bin/env python3
"""
File Organizer Script
A simple tool to organize files in a directory based on various criteria.
"""

import os
import shutil
from pathlib import Path
import datetime
import hashlib
from config import load_config


def get_file_category(file_path, config=None):
    """Determine the category of a file based on its extension."""
    if config is None:
        config = load_config()
    
    extension = Path(file_path).suffix.lower()
    
    for category, extensions in config["file_types"].items():
        if extension in extensions:
            return category
    
    return 'others'


def organize_by_type(source_dir):
    """Organize files by their type/extension."""
    config = load_config()
    source_path = Path(source_dir)
    
    for file_path in source_path.iterdir():
        if file_path.is_file():
            category = get_file_category(file_path, config)
            
            category_dir = source_path / category
            category_dir.mkdir(exist_ok=True)
            
            dest_path = category_dir / file_path.name
            
            try:
                shutil.move(str(file_path), str(dest_path))
                print(f"Moved {file_path.name} to {category}/")
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")


def get_file_hash(file_path):
    """Calculate MD5 hash of a file."""
    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def find_duplicates(source_dir):
    """Find and handle duplicate files."""
    source_path = Path(source_dir)
    file_hashes = {}
    duplicates = []
    
    for file_path in source_path.rglob('*'):
        if file_path.is_file():
            try:
                file_hash = get_file_hash(file_path)
                if file_hash in file_hashes:
                    duplicates.append((file_path, file_hashes[file_hash]))
                    print(f"Duplicate found: {file_path.name} == {file_hashes[file_hash].name}")
                else:
                    file_hashes[file_hash] = file_path
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    
    if duplicates:
        duplicates_dir = source_path / "duplicates"
        duplicates_dir.mkdir(exist_ok=True)
        
        for duplicate, _ in duplicates:
            dest_path = duplicates_dir / duplicate.name
            counter = 1
            while dest_path.exists():
                stem = duplicate.stem
                suffix = duplicate.suffix
                dest_path = duplicates_dir / f"{stem}_{counter}{suffix}"
                counter += 1
            
            try:
                shutil.move(str(duplicate), str(dest_path))
                print(f"Moved duplicate {duplicate.name} to duplicates/")
            except Exception as e:
                print(f"Error moving duplicate {duplicate.name}: {e}")
    
    return len(duplicates)


def organize_by_date(source_dir):
    """Organize files by their modification date."""
    source_path = Path(source_dir)
    
    for file_path in source_path.iterdir():
        if file_path.is_file():
            mod_time = datetime.datetime.fromtimestamp(file_path.stat().st_mtime)
            year_month = mod_time.strftime("%Y-%m")
            
            date_dir = source_path / year_month
            date_dir.mkdir(exist_ok=True)
            
            dest_path = date_dir / file_path.name
            
            try:
                shutil.move(str(file_path), str(dest_path))
                print(f"Moved {file_path.name} to {year_month}/")
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")


def main():
    print("File Organizer v0.3")
    
    source_dir = input("Enter source directory path: ")
    if not os.path.exists(source_dir):
        print("Directory does not exist!")
        return
    
    print("Choose organization method:")
    print("1. By file type")
    print("2. By date")
    print("3. Find duplicates")
    choice = input("Enter choice (1, 2, or 3): ")
    
    print(f"Organizing files in: {source_dir}")
    
    if choice == "1":
        organize_by_type(source_dir)
    elif choice == "2":
        organize_by_date(source_dir)
    elif choice == "3":
        dup_count = find_duplicates(source_dir)
        print(f"Found and moved {dup_count} duplicate files")
    else:
        print("Invalid choice!")
        return
    
    print("Organization complete!")


if __name__ == "__main__":
    main()