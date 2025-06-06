#!/usr/bin/python3
""" Building out BaseGeometry """


class BaseGeometry():
    """ Base Geometry with area() and integer_validator()"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return (value)
