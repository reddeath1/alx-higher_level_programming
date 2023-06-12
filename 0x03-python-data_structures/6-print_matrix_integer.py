#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    print a matrix of integers to STDOUT
    """
    for row in matrix:
        count = len(row)
        for i in range(count):
            if i != count - 1:
                print("{:d}".format(row[i]), end=' ')
            else:
                print("{:d}".format(row[i]), end='')
        print()
