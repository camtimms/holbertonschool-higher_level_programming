#!/usr/bin/python3
"""
A function that returns true if the object is exactly an instance of the
specified class
"""


def is_same_class(obj, a_class):
    """ Compares if a object is an exact match to a class """
    return (type(obj) is a_class)
