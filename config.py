"""
Configuration management for File Organizer Script
"""

import json
import os
from pathlib import Path


DEFAULT_CONFIG = {
    "file_types": {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
        "documents": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
        "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
        "code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".h", ".php", ".rb"]
    },
    "default_organize_method": "type",
    "create_duplicates_folder": True,
    "date_format": "%Y-%m"
}


def get_config_path():
    """Get the configuration file path."""
    home = Path.home()
    config_dir = home / ".file_organizer"
    config_dir.mkdir(exist_ok=True)
    return config_dir / "config.json"


def load_config():
    """Load configuration from file or create default if not exists."""
    config_path = get_config_path()
    
    if config_path.exists():
        try:
            with open(config_path, 'r') as f:
                config = json.load(f)
                return {**DEFAULT_CONFIG, **config}
        except Exception as e:
            print(f"Error loading config: {e}")
            return DEFAULT_CONFIG
    else:
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG


def save_config(config):
    """Save configuration to file."""
    config_path = get_config_path()
    
    try:
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False


def add_file_type(category, extension, config=None):
    """Add a new file type to configuration."""
    if config is None:
        config = load_config()
    
    if category not in config["file_types"]:
        config["file_types"][category] = []
    
    if extension not in config["file_types"][category]:
        config["file_types"][category].append(extension)
        save_config(config)
        return True
    
    return False