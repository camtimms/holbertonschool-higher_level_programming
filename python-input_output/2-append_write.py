#!/usr/bin/python3
"""
Name: append_write
Description: Appends a str to end of text file
Return: Number of characters added (int)
"""


def append_write(filename="", text=""):
    """filename: Name of file, text: str to append"""
    with open(filename, 'a', encoding="utf-8") as f:
        return(f.write(text))
