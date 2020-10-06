#!/usr/bin/python3
""" module that contains add attribute """


def add_attribute(obj, name, value):
    """ add an attirubute if it's possible """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError('can\'t add new attribute')
