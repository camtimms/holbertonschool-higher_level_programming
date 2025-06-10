#!/usr/bin/python3
"""
A function that returns true if the object is inherited from
a specified class
"""


def inherits_from(obj, a_class):
    """ Compares if a object is inherited from a class """
    # Check for exact matach as it's not a child of a_class
    if type(obj) is a_class:
        return (False)
    else:
        return (issubclass(type(obj), a_class))
