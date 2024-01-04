from app import app
from app.config import read_config
from lib.extractor import copy_kindle_clippings
from parse import parse_to_json

config = read_config()
dest_folder = config['extract']['destination_path']
used_os=config['extract']['which_os']

try:
    if config['extract']['enabled']:
        copy_kindle_clippings(dest_folder, used_os)
except Exception as copy_error:
    print(f"Error during copy_kindle_clippings: {str(copy_error)}")
else:
    try:
        if config['parse']['enabled']:
            parse_to_json()
    except Exception as parse_error:
        print(f"Error during parse_to_json: {str(parse_error)}")

if __name__ == '__main__':
    app.run()
