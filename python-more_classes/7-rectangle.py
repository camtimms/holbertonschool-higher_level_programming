#!/usr/bin/python3
"""
Module Documentation: Rectangle Class
"""


class Rectangle:
    """
    Rectangle with width, height, area and perimeter
    """

    number_of_instances = 0
    print_symbol = "#"

    # Initalise Atributes
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates area"""
        area = self.height * self.width
        return (area)

    def perimeter(self):
        """calculates perimeter"""
        if self.height == 0 or self.width == 0:
            return (0)
        perimeter = 2*(self.height + self.width)
        return (perimeter)

    def __str__(self):
        """A method that returns a rectangle with the print_symbol character"""
        if self.height == 0 or self.width == 0:
            return ("")
        rectangle = ""
        for i in range(self.height):
            for j in range(self.width):
                rectangle += str(self.print_symbol)
            if i < self.height - 1:
                rectangle += "\n"
        return (rectangle)

    def __repr__(self):
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
