#!/usr/bin/python3
'''
Module for dividing all elements of a matrix

Divides each element of a matrix by a divisor
'''

def matrix_divided(matrix, div):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    prev_row_len = None
    for row in matrix:
        if prev_row_len is None:
            prev_row_len = len(row)
        if len(row) != prev_row_len:
            raise TypeError("Each row of the matrix must have the same size")
        prev_row_len = len(row)
    
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [list(map(lambda x: round(x/div, 2), row)) for row in matrix]

    return (new_matrix)
