#!/usr/bin/python3
""" module that contains the append write"""


def append_write(filename="", text=""):
    """ appends a string to end of txt file"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
