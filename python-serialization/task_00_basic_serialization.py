#!/usr/bin/python3
"""
Basic Serialization

Description: A module to learning about how to serialize a Python dict into a
JSON file and from a JSON file back into a Python dict
"""
import pickle


def serialize_and_save_to_file(data, filename):
    """
    data: A python dict with data
    filename: The filename of the output JSON file.
    """
    try:
        with open(filename, 'wb') as f:
            return (pickle.dump(data, f))
    except TypeError:
        raise TypeError("Error: Non-serializable object")


def load_and_deserialize(filename):
    """
    filename:  The filename of the input JSON file

    Description: This function returns a Python Dictionary with the deseialized
    JSON data from the file.
    """
    try:
        with open(filename, "rb") as f:
            return (pickle.load(f))
    except TypeError:
        raise TypeError("Error: File is non-serializable")
