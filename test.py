#!/usr/bin/env python3

# Test script

import subprocess, os
import random as rnd
from clean import clean_folder

# Global variables

seed = "qwertyuiopasdfghjklzxcvbnm1234567890"

def rand_string(seed: str) -> str:
    s = ''
    max_len = len(seed)
    s_len = rnd.randint(1, len(seed))

    while (len(s) < s_len):
        s = s + seed[rnd.randint(0,max_len-1)]
    
    return s


def main():
    # Create a dummy test folder with files in it
    folder = "testfolder"

    os.system(f'mkdir {folder}')

    # Generate n random files
    for i in range(10):
        n = rnd.randint(1, 30)
        s = rand_string(seed)
        path = folder + '/' + f'file{i}.txt' 
        os.system(f'touch {path} && echo {s} > {path}')

    # Try deleting content in folder
    clean_folder(folder)

    # Check if folder is empty
    assert not os.listdir(f'./{folder}')

    os.system(f'rm -rf {folder}')

    print('Test passed')

if __name__ == "__main__":
    main()
