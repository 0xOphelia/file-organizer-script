#!/usr/bin/env python3
"""
File Organizer Script
A simple tool to organize files in a directory based on various criteria.
"""

import os
import shutil
from pathlib import Path


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


def main():
    print("File Organizer v0.1")
    
    source_dir = input("Enter source directory path: ")
    if not os.path.exists(source_dir):
        print("Directory does not exist!")
        return
    
    print(f"Organizing files in: {source_dir}")
    organize_by_type(source_dir)
    print("Organization complete!")


if __name__ == "__main__":
    main()