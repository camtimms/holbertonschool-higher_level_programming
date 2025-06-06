#!/usr/bin/python3
""" New Class Rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle which inherits from BaseGeometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        __width = width
        __height = height
