#!/usr/bin/python3
"""
Name: load_from_json_file
Description: Creates an object from a JSON file
Returns: (Obj)
"""
import json


def load_from_json_file(filename):
    """filename: Name of file"""
    with open(filename, 'r') as f:
        return (json.load(f))
