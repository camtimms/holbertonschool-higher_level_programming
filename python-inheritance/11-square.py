#!/usr/bin/python3
""" New Class Square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square which inherits from Rectangle which inherits
    from BaseGeometry """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        area = self.__size**2
        return (area)

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
