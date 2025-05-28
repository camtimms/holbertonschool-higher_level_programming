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
        """Calculate the size of a square"""
        return (self._Square__size**2)
    
    @property
    def size(self):
        """Getter for size"""
        return (self._Square__size)
    
    @size.setter
    def size(self, value):
        """Setter for size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value
