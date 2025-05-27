#!/usr/bin/python3
"""
This is a module for the text_indentation function
"""


def text_indentation(text):
    """
    This prints two newline characters after every ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        char = text[i]
        print(char, end="")
        if char in (".", "?", ":"):
            print("\n\n", end="")
            if i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i +=1