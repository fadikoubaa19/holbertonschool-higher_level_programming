#!/usr/bin/python3
"""this module contain my_int"""


class MyInt(int):
    def __init__(self, value):
        self.value = value

    def __eq__(self, obj):
        return (obj != self.value)

    def __ne__(self, obj):
        return (obj == self.value)
