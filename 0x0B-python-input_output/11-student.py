#!/usr/bin/python3
"""module that  contains  Student """


class Student:
    """ class student """

    def __init__(self, first_name, last_name, age):
        """ function init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ the  representation of  Student instance """
        return self.__dict__
