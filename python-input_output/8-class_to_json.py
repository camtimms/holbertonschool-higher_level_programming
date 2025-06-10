#!/usr/bin/python3
"""
Name: class_to_json
Description: Converts an instance of a class to a JSON object
Returns: JSON Object (dict)
"""
import json


def class_to_json(obj):
    """obj: Instance of a class"""
    return (json.dumps(obj.__dict__))
