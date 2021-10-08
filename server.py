#!/usr/bin/env python3

# Paolo Anzani <p.anzani@campus.unimib.it> 10-07-2021

# Serve UI app on localhost

from flask import Flask, request
import os, subprocess, json

# Flask settings
app = Flask(__name__, static_url_path="/ui", static_folder='./ui')

# Load html files
index = open("ui/index.html", "r").read()

@app.route("/")
def main():
    return index

# Dialog GUI activation end-point
@app.route("/dialog", methods=['POST'])
def dialog():
    if request.method == 'POST':
        path = str(subprocess.check_output(['python3', 'dialog.py']))

        if path[2:-3] == '':
            status = 'error'
            code = 501
        else:
            status = 'succes'
            code = 201

        response = json.dumps({'data': path[2:-3], 'status': status, 'code': code})
        print(path) # Log it in the console
        return response
    else:
        return 'wrong type request'

if __name__ == "__main__":
    app.run()




    

