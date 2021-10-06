#!/usr/bin/env python3

# Version 1.0

# Mac-OS junk cleaner script
# Latest tested version Mac-OS Big Sur 11.5

# Launch the script from the terminal app or it will not work properly

import subprocess, os, argparse, shutil
from typing import NewType, List
from parsing import reader

# CLI argument parsing

parser = argparse.ArgumentParser(description='Clean Mac-OS junk.')
parser.add_argument('--full', action='store_true', help='Full disk cleaning')
parser.add_argument('config', type=str, help='Config file path')

# Custom types

Folder_list = NewType('Folder_list', List[str])

# Global variables

args = parser.parse_args()

root_home = os.getenv("HOME")

folders = Folder_list(reader(args.config, "folders"))
          
folders_full = Folder_list(reader(args.config, "folders_full"))

# Delete a given folder

def clean_folder(folder: str):
    folder = folder.replace("~", root_home)
    # List all the content of a dir
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        # Check if file or directory
        if os.path.isfile(file_path) or os.path.islink(file_path):
            subprocess.call(['sudo', 'rm', file_path])
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
            
# Main function

def main():
    for f in folders:
        clean_folder(f)
    
    # if --full is passed execute full clean
    if args.full:
        for f in folders_full:
            clean_folder(f)
        # A system reboot is necessary when deleting /private/var/folders content
        subprocess.call(['sudo', 'reboot'])

    print("Cleaning complete")


if __name__ == "__main__":

    main()
