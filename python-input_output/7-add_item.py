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


def add_item(filename):
    """obj: Object to add, filename: Name of file"""
    try:
        my_list = load_to_json_file(filename)
    except FileNotFoundError:
        my_list = []

    for arg in sys.argv[1:]:
        my_list.append(arg)

    save_to_json_file(my_list, filename)


add_item("add_item.json")
