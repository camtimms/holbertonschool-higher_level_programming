#!/usr/bin/python3
"""
Name: add_item
Description: Adds an item to a list then saves it to file
Returns: None
"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_to_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_item(arg, filename):
    """obj: Object to add, filename: Name of file"""
    try:
        list = load_to_json_file(filename)
    except FileNotFoundError:
        list = save_to_json_file("", filename)
    for arg in sys.argv[1:]:
        list.append(arg)
    save_to_json_file(list, filename)


add_item(sys.argv, "add_item.json")
