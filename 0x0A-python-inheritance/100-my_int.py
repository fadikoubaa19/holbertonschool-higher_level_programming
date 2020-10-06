#!/usr/bin/python3
""" modue that contains my int"""


class MyInt(int):

    def __init__(self, value):
        """function init"""
        self.value = value

    def __eq__(self, other):
        """function equal =!"""
        return(self.value != other)

    def __ne__(self, other):
        """function equal =="""
        return(self.value == other)
