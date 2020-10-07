#!/usr/bin/python3
""" module that contaile read function """


def read_file(filename=""):
    """ read file .txt """
    with open(filename, encoding='utf-8') as t:
        for line in t:
            print(line, end="")
