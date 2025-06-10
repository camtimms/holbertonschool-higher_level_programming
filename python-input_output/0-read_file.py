#!/usr/bin/python3
"""
Name: read_file
Description: A function that reads a file and prints to stout
Return: None
"""

def read_file(filename=""):
    """filename: Name of file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read())
