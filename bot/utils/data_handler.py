def load_data(file_path):
    """Load data from a JSON file."""
    import json
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_data(file_path, data):
    """Save data to a JSON file."""
    import json
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)