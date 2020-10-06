#!/usr/bin/python3
"""
This module contain my int
"""


class MyInt(int):
    """
    define class
    """
    def __init__(self, value):
        """
        function init
        """
        self.value = value

    def __eq__(self, obj):
        """
        overrides the equal int method
        """
        return (obj != self.value)

    def __ne__(self, obj):
        """
        function not equal
        """
        return (obj == self.value)
