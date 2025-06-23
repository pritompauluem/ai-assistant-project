import os
import json
from datetime import datetime

def ensure_directory_exists(path):
    """
    Ensures that a directory exists. If it doesn't, it creates it.
    """
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def log_event(message, log_file="data/logs.txt"):
    """
    Logs an event with a timestamp to a specified log file.
    """
    ensure_directory_exists(os.path.dirname(log_file))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] {message}\n")
    print(f"Logged: {message}")

def load_json(filepath, default_value=None):
    """
    Loads JSON data from a file. Returns default_value if file doesn't exist or is empty.
    """
    try:
        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            return default_value if default_value is not None else []
        with open(filepath, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        log_event(f"Error decoding JSON from {filepath}. Returning default value.", "data/errors.log")
        return default_value if default_value is not None else []
    except Exception as e:
        log_event(f"An unexpected error occurred while loading {filepath}: {e}", "data/errors.log")
        return default_value if default_value is not None else []

def save_json(filepath, data):
    """
    Saves data to a JSON file.
    """
    ensure_directory_exists(os.path.dirname(filepath))
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        log_event(f"An unexpected error occurred while saving to {filepath}: {e}", "data/errors.log")

