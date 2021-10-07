# Paolo Anzani <p.anzani@campus.unimib.it> 10-07-2021

# Log functions to track removed file size

import os

def log_size(file_name: str):
    size = os.stat(file_name).st_size
    print(file_name, size, "bytes")
