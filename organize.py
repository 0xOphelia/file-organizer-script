#!/usr/bin/env python3
"""
File Organizer Script
A simple tool to organize files in a directory based on various criteria.
"""

import os
import shutil
from pathlib import Path


def main():
    print("File Organizer v0.1")
    
    source_dir = input("Enter source directory path: ")
    if not os.path.exists(source_dir):
        print("Directory does not exist!")
        return
    
    print(f"Organizing files in: {source_dir}")


if __name__ == "__main__":
    main()