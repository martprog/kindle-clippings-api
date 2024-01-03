import json
from lib.parser import parse_clippings
from app.config import read_config

config = read_config()
source_file= config['parse']['source_file']
dest_file= config['parse']['output_file']

#Parse to json from .txt file
def parse_to_json():
    try:
        clippings_list = parse_clippings(source_file)
    except Exception as e:
        print(f"Error parsing clippings: {e}")
        return

    try:
        # Save the clippings to a JSON file
        with open(dest_file, 'w', encoding='utf-8') as output_file:
            json.dump(clippings_list, output_file, indent=2)
        print(f'Parsed clippings saved to {dest_file}')
    except Exception as e:
        print(f"Error saving clippings to JSON: {e}")

#read json for Views
def read_json_file():
    try:
        with open(dest_file, 'r') as file:
            quotes_data = json.load(file)
        return quotes_data
    except FileNotFoundError:
        print(f"The file '{dest_file}' does not exist.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in '{dest_file}': {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None