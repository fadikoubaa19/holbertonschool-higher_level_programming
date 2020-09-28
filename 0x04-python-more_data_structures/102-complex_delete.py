#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    a_dict = a_dictionary.copy()
    for pos in a_dict:
        if a_dictionary[pos] == value:
            del a_dictionary[pos]
    return a_dictionary
