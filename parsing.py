# Paolo Anzani <p.anzani@campus.unimib.it> 10-06-2021

# JSON parser for folders list

import json, os


def reader(file_path: str, key: str) -> list:
    # Open JSON file
    fp = open(file_path)

    # Parsing JSON file
    _json = json.loads(fp.read())

    l = _json[key]
    return l
