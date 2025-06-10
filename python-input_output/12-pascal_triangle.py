#!/usr/bin/python3
"""
Name: pascal_triangle
Description: Returns a list of ints in the form of pascals triangle
Return: List of list of ints
"""


def pascal_triangle(n):
    if n <= 0:
        return ([])

    pascal_triangle = [[1]]

    for i in range(1, n):
        prev_term = pascal_triangle[i-1]
        new_term = [1]

        for j in range(1, len(prev_term)):
            new_term.append(prev_term[j-1] + prev_term[j])
        new_term.append(1)
        pascal_triangle.append(new_term)

    return (pascal_triangle)
