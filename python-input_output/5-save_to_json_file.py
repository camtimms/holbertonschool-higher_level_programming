#!/usr/bin/python3
"""
Name: save_to_json_file
Description: Writes an obj to a text file using JSON representation
Returns: None
"""
import json


def save_to_json_file(my_obj, filename):
    """my_obj: Object to save, filename: Name of file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json_str = json.dumps(my_obj)
        f.write(json_str)
