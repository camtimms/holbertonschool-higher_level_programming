#!/usr/bin/python3
"""
Name: write_file
Description: Writes a str to file
Return: Number of characters (int)
"""


def write_file(filename="", text=""):
    """filename: Name of file, text: String to write"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
