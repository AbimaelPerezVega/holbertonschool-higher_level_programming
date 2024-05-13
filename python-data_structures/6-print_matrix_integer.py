#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for element in x:
            print("{:d}".format(element), end=" "if element != x[-1] else "")
        print()
