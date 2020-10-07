#!/usr/bin/python3
"""module contains function that read lines"""


def read_lines(filename="", nb_lines=0):
    """ return the n lines"""
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
        f.seek(0)
        if 0 < nb_lines < lines:
            for i in range(nb_lines):
                print(f.readline(), end="")
                i += 1
        else:
            for line in f:
                print(line, end="")
