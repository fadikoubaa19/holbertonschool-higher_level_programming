#!/usr/bin/python3
""" module contains the function of number of lines """


def number_of_lines(filename=""):
    """ returns the number of file txt """
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
