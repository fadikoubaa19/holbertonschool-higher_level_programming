#!/usr/bin/python3
"""
This module add a better setattr function
"""


def add_attribute(obj, name, value):
    """ add an attribute to a class if possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
