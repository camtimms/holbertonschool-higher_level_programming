#!/usr/bin/python3
"""
Module documentation: Creating bounds for the size atribute
"""


class Square:
    """
    A class square which holds an atribute size
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
