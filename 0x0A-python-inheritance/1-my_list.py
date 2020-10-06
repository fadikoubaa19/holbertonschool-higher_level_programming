#!/usr/bin/python3
""" print a list but sorted"""


class MyList(list):
    """Mylist"""
    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
