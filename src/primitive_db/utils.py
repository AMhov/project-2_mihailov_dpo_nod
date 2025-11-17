import json
import os
from util_read_config import read_config

filepath = read_config().get('FILEPATH')


def load_metadata(filepath):
    try:
        # Проверяем размер файла перед чтением (начало работы с пустой базой)
        if os.path.getsize(filepath) == 0:
            print(f"Файл метаданных - '{filepath}', пустой.")
            return {}
            
        with open(filepath, 'r') as f:
            metadata = json.load(f)
            return metadata
    except FileNotFoundError:
        print(f"Нет файла метаданных - '{filepath}'.")
        return {}
    

def save_metadata(filepath, data):
    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving metadata: {e}")
    