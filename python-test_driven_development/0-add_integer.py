#!/usr/bin/python3
"""
Module for integer addition operations.

This module provides a function to add two integers with proper type checking
and error handling.
"""


def add_integer(a, b=98):
    """
    Given two integers, return the sum.

    :param a: int
    :param b: int
    :return: int

    >>> add_integer(2, 3)
    5
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
