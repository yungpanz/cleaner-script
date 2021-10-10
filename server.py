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
@app.route("/dialog", methods=['GET'])
def dialog():
    if request.method == 'GET':
        path = str(subprocess.check_output(['python3', 'dialog.py']))

        if path[2:-3] == '':
            status = 'error'
            code = 501
        else:
            status = 'success'
            code = 201

        response = json.dumps({'folder': path[2:-3], 'status': status, 'code': code})
        print(f'path selected: {path}') # Log it in the console
        return response
    else:
        return 'wrong type request'

# Export and safe config file end-point
@app.route("/export", methods=['POST'])
def export():
    if request.method == 'POST':
        data = json.dumps(request.json).replace('\\\\', '\\')
        print(f'export data recived: {data}') # Log it to the console

        fp = open("config.json", "w")
        fp.write(data)
        fp.close()
        print('data saved!')
        
        return 'export success'
    else:
        return 'wrong type request'

if __name__ == "__main__":
    app.run(ssl_context='adhoc')




    

