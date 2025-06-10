#!/usr/bin/python3
"""
Name: to_json_string
Description: Returns the JSON representation as a str
Return: JSON formatted string
"""
import json


def to_json_string(my_obj):
    """my_obj: Object to convert"""
    return (json.dumps(my_obj))
