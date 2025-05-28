#!/usr/bin/python3
"""
Module documentation: Prints a square
"""


class Square:
    """
    A class square which holds an atribute size and calculates
    the area of the square.

    Can now also print the square of the size
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
        self.position = position

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

    @property
    def position(self):
        return (self._position)

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        for item in value:
            if not isinstance(item, int):
                raise TypeError("position must be a tuple of 2 positive"
                                " integers")
            if item < 0:
                raise TypeError("position must be a tuple of 2 positive"
                                " integers")

        self._position = value

    def my_print(self):
        """A function that prints a square with the character #"""
        if self.size == 0:
            print("")
            return

        # Vertical Offset
        vert_offset = 0
        while vert_offset < self.position[1]:
            print("")
            vert_offset += 1

        row = 0
        col = 0

        while row < self.size:

            # Horizontal Offset
            horz_offset = 0
            while horz_offset < self.position[0]:
                print(" ", end="")
                horz_offset += 1

            col = 0
            while col < self.size:
                print("#", end="")
                col += 1
            print("")
            row += 1
