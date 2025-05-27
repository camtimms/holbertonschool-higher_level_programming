#!/usr/bin/python3
"""
Module for print_square
"""


def print_square(size):
    """
    A function that prints a square with the character #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    row = 0
    col = 0

    while row < size:
        col = 0
        while col < size:
            print("#", end="")
            col += 1
        print("")
        row += 1
