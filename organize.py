#!/usr/bin/env python3
"""
File Organizer Script
A simple tool to organize files in a directory based on various criteria.
"""

import os
import shutil
from pathlib import Path
import datetime


FILE_TYPES = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt'],
    'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv'],
    'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
    'archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'code': ['.py', '.js', '.html', '.css', '.cpp', '.java', '.c']
}


def get_file_category(file_path):
    """Determine the category of a file based on its extension."""
    extension = Path(file_path).suffix.lower()
    
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    
    return 'others'


def organize_by_type(source_dir):
    """Organize files by their type/extension."""
    source_path = Path(source_dir)
    
    for file_path in source_path.iterdir():
        if file_path.is_file():
            category = get_file_category(file_path)
            
            category_dir = source_path / category
            category_dir.mkdir(exist_ok=True)
            
            dest_path = category_dir / file_path.name
            
            try:
                shutil.move(str(file_path), str(dest_path))
                print(f"Moved {file_path.name} to {category}/")
            except Exception as e:
                print(f"Error moving {file_path.name}: {e}")


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
    print("File Organizer v0.2")
    
    source_dir = input("Enter source directory path: ")
    if not os.path.exists(source_dir):
        print("Directory does not exist!")
        return
    
    print("Choose organization method:")
    print("1. By file type")
    print("2. By date")
    choice = input("Enter choice (1 or 2): ")
    
    print(f"Organizing files in: {source_dir}")
    
    if choice == "1":
        organize_by_type(source_dir)
    elif choice == "2":
        organize_by_date(source_dir)
    else:
        print("Invalid choice!")
        return
    
    print("Organization complete!")


if __name__ == "__main__":
    main()