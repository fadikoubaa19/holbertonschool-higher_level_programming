#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename) as file:
        lines = len(file.read())
    return(lines)

