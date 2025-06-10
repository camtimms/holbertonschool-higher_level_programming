#!/usr/bin/python3
"""
Name: from_json_string
Description: Returns JSON object from string
Returns: JSON object
"""
import json


def from_json_string(my_str):
    """my_str: String to convert to JSON"""
    return (json.loads(my_str))
