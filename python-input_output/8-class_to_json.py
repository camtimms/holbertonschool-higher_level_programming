#!/usr/bin/python3
"""
Name: class_to_json
Description: Converts an instance of a class to a JSON object
Returns: JSON Object (dict)
"""


def class_to_json(obj):
    """obj: Instance of a class"""
    return (obj.__dict__)
