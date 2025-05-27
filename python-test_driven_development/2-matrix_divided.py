#!/usr/bin/python3
'''
Module for dividing all elements of a matrix

Divides each element of a matrix by a divisor
'''


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix: A list of lists containing integers or floats
        div: The number to divide by (int or float, cannot be 0)

    Returns:
        A new matrix with all elements divided by div, rounded to 2 dp

    Raises:
        TypeError: If matrix is not a list of lists of ints/floats
        TypeError: If rows of matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    prev_row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists)"
                            " of integers/floats")
        if prev_row_len is None:
            prev_row_len = len(row)
        if len(row) != prev_row_len:
            raise TypeError("Each row of the matrix must have the same size")
        prev_row_len = len(row)
        for element in row:
            if type(element) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of"
                                " integers/floats")

    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [list(map(lambda x: round(x/div, 2), row)) for row in matrix]

    return (new_matrix)
