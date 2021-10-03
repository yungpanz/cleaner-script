#!/usr/bin/env python3

# Version 1.0

# Mac-OS junk cleaner script
# Latest tested version Mac-OS Big Sur 11.5

# Launch the script from the terminal app or it will not work properly

import subprocess, os, argparse, shutil
from typing import NewType, List

# CLI argument parsing

parser = argparse.ArgumentParser(description='Clean Mac-OS junk.')
parser.add_argument('--full', action='store_true', help='Full disk cleaning')

# Custom types

Folder_list = NewType('Folder_list', List[str])

# Global variables

args = parser.parse_args()

root_home = '/Users/paoloanzani'

folders = Folder_list(["~/.cache", '~/.pub-cache', '/usr/local/var/cache',
                        '~/.cargo/registry/cache', '~/Library/Caches/vscode-cpptools',
                        '~/Library/Caches/typescript', '~/Library/Caches/pip',
                        '~/Library/Containers/com.apple.Mail/Data/Library/Caches',
                        '~/Library/Containers/com.apple.Safari/Data/Library/Caches'])

folders_extra = Folder_list(['~/Library/Caches/Google/Chrome', '~/Library/Caches/com.spotify.client',
                              '/private/var/folders'])

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
        for f in folders_extra:
            clean_folder(f)
        # A system reboot is necessary when deleting /private/var/folders content
        subprocess.call(['sudo', 'reboot'])

    print("Cleaning complete")


if __name__ == "__main__":

    main()
