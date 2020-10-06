#!/usr/bin/python3
""" contains class BaseGeometry """


class BaseGeometry:
    """ defines class BaseGeometry """

    def area(self):
        """ raises Exception """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ check value as a postif integer"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
