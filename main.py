#!/usr/bin/env python3
# Paolo Anzani <p.anzani@campus.unimib.it> 10-05-2021

# Version 1.1

# Mac-OS junk cleaner script
# Latest tested version Mac-OS Big Sur 11.5

# Launch with sudo

import subprocess, os, argparse, shutil
from typing import NewType, List
from parsing import reader
from logger import log_size

# CLI argument parsing

parser = argparse.ArgumentParser(description='Clean Mac-OS junk.')
parser.add_argument('--full', action='store_true',
                    help='Full disk cleaning')
parser.add_argument('config', type=str, help='Config file path')

# Custom types

Folder_list = NewType('Folder_list', List[str])

# Global variables

args = parser.parse_args()

root_home = os.getenv("HOME")

folders = Folder_list(reader(args.config, "folders"))
          
folders_full = Folder_list(reader(args.config, "folders_full"))

# Delete a given folder

def clean_folder(folder: str) -> int:
    folder = folder.replace("~", root_home)
    bytes_count = 0
    # List all the content of a dir
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        # Check if file or directory
        if os.path.isfile(file_path) or os.path.islink(file_path):
            bytes_count += log_size(file_path)
            subprocess.call(['rm', file_path])
        elif os.path.isdir(file_path):
            bytes_count += log_size(file_path)
            shutil.rmtree(file_path)
    return bytes_count
            
# Main function

def main():
    removed_size = 0
    for f in folders:
        removed_size += clean_folder(f)
    
    # if --full is passed execute full clean
    if args.full:
        for f in folders_full:
            removed_size += clean_folder(f)

    print(f'Total space cleaned: {removed_size} bytes')

if __name__ == "__main__":

    main()
