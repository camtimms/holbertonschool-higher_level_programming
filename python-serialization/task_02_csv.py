#!/usr/bin/python3
"""
Converting CSV to JSON

The objective of this exercise is to gain experience in reading data from one
format (CSV) and converting it into another format (JSON) using serialization
techniques.
"""
import csv, json

def convert_csv_to_json(filename):
    try:
        with open(filename) as file:
            formatted_data = list(csv.DictReader(file))
        with open("data.json", "w") as json_file:
            json.dump(formatted_data, json_file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return (False)

    return(True)

