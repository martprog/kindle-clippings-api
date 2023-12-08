import argparse
import subprocess
import os

def get_current_user():
    return subprocess.check_output(['whoami']).decode().strip()

def copy_kindle_clippings(destination_path, kindle_name=None):
    if kindle_name is None:
        kindle_name = get_current_user()
    kindle_mount_point = f"/media/{kindle_name}"

    # Check if the Kindle is mounted and copy the file.
    if subprocess.run(['test', '-d', kindle_mount_point]).returncode == 0:
        source_file = f"{kindle_mount_point}/Kindle/documents/My Clippings.txt"
        # Copy the "my clippings.txt" file
        if os.path.exists(source_file):
            dest_file = destination_path 
            try:
                subprocess.run(['cp', source_file, dest_file], check=True)
                print(f"Copied 'my clippings.txt' to {destination_path}")
            except subprocess.CalledProcessError as e:
                print(f"Error during file copy: {e}")
    else:
        print("Kindle not found. Make sure it's plugged in and mounted.")

#To use the extract action autonomously. In this case, the destination file must be passed as an argument
if __name__ == "__main__":  
    default_kindle_name = get_current_user()
    parser = argparse.ArgumentParser(description="Copy 'my clippings.txt' from Kindle to a specified folder.")
    parser.add_argument("destination_path", help="Destination directory for the copied file.")
    parser.add_argument("--kindle_name", default=default_kindle_name, help="Name of the connected Kindle device (default is the current user).")

    args = parser.parse_args()

    copy_kindle_clippings(args.destination_path, args.kindle_name)
