#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        a = ""
        for j in range(len(matrix[i])):
            print(a, end="")
            print("{:d}".format(matrix[i][j]), end="")
            a = " "
        print()
