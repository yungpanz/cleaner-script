#!/usr/bin/env python3
# Paolo Anzani <p.anzani@campus.unimib.it> 10-10-2021

# Launch UI

import webbrowser as wb
import subprocess

# Global variables
url = 'http://localhost:8080/'

def main():
    # Open in a new window if not already open
    wb.open_new(url)
    # Start server
    subprocess.run(["python3", "server.py"])

    
if __name__ == "__main__":
    main()
