#!/usr/bin/python3
class MyInt(int):
    """ defines class MyInt """

    def __eq__(self, other):
        """ function faking """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """function faking """
        return int.__eq__(self, other)
