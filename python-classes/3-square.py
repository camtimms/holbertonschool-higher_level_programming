#!/usr/bin/python3
"""
Module documentation: Adding in a new method to calculate the
 area of the square
"""


class Square:
    """
    A class square which holds an atribute size and calculates
    the area of the square
    """
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        self.area = self._Square__size**2
        return (self.area)
