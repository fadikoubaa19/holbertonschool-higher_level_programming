#!/usr/bin/python3
""" module contaien the square """

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines class Square """

    def __init__(self, size):
        """ empty square """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)
