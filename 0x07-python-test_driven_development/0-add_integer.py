#!/usr/bin/python3
''' a function that  add two integers
'''


def add_integer(a, b=98):
    ''' add_integer simple function
    args
    a, b'''

    try:
        if isinstance(a, float):
            raise TypeError
    except TypeError:
        a = int(a)

    try:
        if isinstance(b, float):
            raise TypeError
    except TypeError:
        b = int(b)

    try:
        if not(isinstance(a, int)):
            raise TypeError
    except:
        raise TypeError('a must be an integer')

    try:
        if not(isinstance(b, int)):
            raise TypeError
    except:
        raise TypeError('b must be an integer')
    return (a + b)
