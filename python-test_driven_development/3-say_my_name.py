#!/usr/bin/python3
"""
Module for say_my_name

Function that prints the users name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints the users name
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
