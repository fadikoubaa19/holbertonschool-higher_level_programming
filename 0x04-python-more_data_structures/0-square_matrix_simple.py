#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    a = list(map(lambda x: list(map(lambda y: y * y, x)), matrix))
    return (a)
