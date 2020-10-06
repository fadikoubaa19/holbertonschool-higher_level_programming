#!/usr/bin/python3
""" module full rectangme"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines class Rectangle """

    def __init__(self, width, height):
        """ init function that validate
            a positive integer for height and width"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ returns area of Rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns the  string representation of Rectangle """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
