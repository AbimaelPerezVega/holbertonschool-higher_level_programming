#/usr/bin/python3^M
"""This script adds all arguments to a Python list and then saves
them to a file as a JSON representation."""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

json_file = 'add_item.json'

try:
    data = load_from_json_file(json_file)
except FileNotFoundError:
    data = []

for arg in sys.argv[1:]:
    data.append(arg)

save_to_json_file(data, json_file)