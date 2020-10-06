#!/usr/bin/python3
""" True if the object is an instance of a class t"""


def inherits_from(obj, a_class):
    """an instance of a class that inherited directly or indirectly"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
