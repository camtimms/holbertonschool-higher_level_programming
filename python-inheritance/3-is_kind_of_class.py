#!/usr/bin/python3
"""
A function that returns true if the object is an instance of or inherited from
a specified class
"""


def is_kind_of_class(obj, a_class):
    """ Compares if a object is inherited or a match to a class """
    return (isinstance(obj, a_class))
