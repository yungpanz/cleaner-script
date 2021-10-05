#!/usr/bin/env python3

# Test script

import subprocess
import os
from main import *


def main():
    # Create a dummy test folder with file in it
    folder = "testfolder"
    file_name = "file.txt"
    path = folder + '/' + file_name

    os.system(f'mkdir {folder}')
    os.system(f'touch {path}')

    # Try deleting content in folder
    clean_folder(folder)

    # Check if folder is empty
    assert not os.listdir(f'./{folder}')

    os.system(f'rm -rf {folder}')

    print('Test passed')

if __name__ == "__main__":
    main()
