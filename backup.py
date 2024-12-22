##############################################################
# Script for making backups of any selected files or folders #
#          version 0.1  12.2024  Oleksii Nizhegolenko        #
#                       MIT License                          #
##############################################################


import os
import zipfile
import argparse
import configparser
from datetime import datetime


# Reading configuration file
def read_config(config_file):
    config = configparser.ConfigParser()
    try:
        config.read(config_file)
        
        source_paths = config.get("source", "paths").split(",")
        source_paths = [
            os.path.normpath(p.strip()) + os.sep if os.path.isdir(p.strip()) else os.path.normpath(p.strip())
            for p in source_paths
        ]

        dest_path = config.get("destination", "path").strip()
        dest_path = [os.path.normpath(dest_path)]

        return source_paths, dest_path
    except(configparser.NoSectionError, configparser.NoOptionError) as e:
        raise ValueError(f"Error reading configuration file: {e}")

# Creating zip file
def create_zip(source_path, output_zip):
   try:
        with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as backup_zip:
            for path in source_path:
                if os.path.isdir(path):
                    for foldername, subfolders, filenames in os.walk(path):
                        for filename in filenames:
                            filepath = os.path.join(foldername, filename)
                            arcname = os.path.relpath(filepath, start=path)
                            backup_zip.write(filepath, arcname=os.path.join(os.path.basename(path), arcname))
                elif os.path.isfile(path):
                    backup_zip.write(path, arcname=os.path.basename(path))
                else:
                    print(f"Warning: Path '{path}' does not exist or is invalid. Skipping...")
   except PermissionError as e:
       print(f"Permission denied: {e}")
   except Exception as e:
       print(f"Error creating ZIP file: {e}")
       

def main():
    # Parsing command-line arguments
    parser = argparse.ArgumentParser(
        description="This script creates backups based on the provided configuration file. "
                    "You must specify a single configuration file using the -c or --config flag."
        )
    parser.add_argument(
        "-c", "--config", required=True, help="Path to the configuration file (only one file allowed)."
    )
    args = parser.parse_args()

    config_path = args.config

    try:
        # Read configuration file
        source_paths,dest_path = read_config(config_path)

        # Ensure destination directory exists
        if not os.path.exists(dest_path[0]):
            os.makedirs(dest_path[0])

        # Generate backup file name with timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_file_name = os.path.join(dest_path[0], f"backup_{timestamp}.zip")

        # Create ZIP archive
        create_zip(source_paths, backup_file_name)

    except FileNotFoundError as e:
        print(f"Configuration file not found: {e}")
    except ValueError as e:
        print(f"Configuration error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
