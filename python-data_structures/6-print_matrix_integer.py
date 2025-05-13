#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if col == len(row):
            print("{:d}".format(col), end="")
        else:
            for col in row:
                print("{:d} ".format(col), end="")
        print()
