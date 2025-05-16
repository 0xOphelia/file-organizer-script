# File Organizer Script

A simple Python tool to automatically organize files in a directory based on various criteria.

## Features

- **File Type Organization**: Sort files into folders by their file extensions
- **Date-based Organization**: Organize files by modification date (YYYY-MM format)
- **Duplicate Detection**: Find and move duplicate files to a separate folder
- **Configurable**: Customize file type categories and extensions
- **Safe**: Creates folders automatically and handles errors gracefully

## Usage

Run the script:

```bash
python organize.py
```

Choose from three organization methods:
1. **By file type** - Sorts files into folders like `images/`, `documents/`, `videos/`, etc.
2. **By date** - Creates folders like `2025-05/`, `2025-04/` based on file modification dates  
3. **Find duplicates** - Identifies duplicate files (by MD5 hash) and moves them to `duplicates/`

## Configuration

The script creates a configuration file at `~/.file_organizer/config.json` on first run.

You can customize:
- File type categories and their extensions
- Date format for date-based organization
- Whether to create a duplicates folder

## File Categories

Default categories:
- **Images**: .jpg, .jpeg, .png, .gif, .bmp, .tiff, .svg, .webp
- **Documents**: .pdf, .doc, .docx, .txt, .rtf, .odt, .xls, .xlsx, .ppt, .pptx  
- **Videos**: .mp4, .avi, .mkv, .mov, .wmv, .flv, .webm
- **Audio**: .mp3, .wav, .flac, .aac, .ogg, .m4a
- **Archives**: .zip, .rar, .7z, .tar, .gz, .bz2
- **Code**: .py, .js, .html, .css, .cpp, .java, .c, .h, .php, .rb
- **Others**: Any file type not in the above categories

## Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## Safety

- The script moves files, not copies them
- Always test on a backup copy of your files first
- Files are moved within the same directory structure