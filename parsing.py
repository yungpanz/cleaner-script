# Paolo Anzani <p.anzani@campus.unimib.it> 10-06-2021

# JSON parser for folders list

import json, os
from main import Folder_list


def reader(file_path: str, key: str) -> Folder_list:
    # Open JSON file
    fp = open(file_path)

    # Parsing JSON file
    _json = json.loads(fp.read())

    l = Folder_list(_json[key])
    return l
