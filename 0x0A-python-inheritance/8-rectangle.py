#!/usr/bin/python3
""" module contains rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines class Rectangle """

    def __init__(self, width, height):
        """ init function that validate width
            and height with positive integer"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", height):
            self.__height = height
