import json

def load_data(file_path) -> dict:
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(file_path: str, data: dict) -> None:
    """Save data to a JSON file."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)