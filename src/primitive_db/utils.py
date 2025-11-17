import json
from util_read_config import read_config

filepath = read_config().get('FILEPATH')


def load_metadata(filepath):
    try:
        with open(filepath, 'r') as f:
            metadata = json.load(f)
            return metadata
    except FileNotFoundError:
        print(f"Error: Metadata file '{filepath}' not found.")
        return {}
    

def save_metadata(filepath, data):
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving metadata: {e}")
    