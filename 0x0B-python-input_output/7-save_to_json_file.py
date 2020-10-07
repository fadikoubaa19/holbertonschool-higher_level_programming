#!/usr/bin/python3
"""module that contains the function of save to json file"""
import json


def save_to_json_file(my_obj, filename):
    """write an obj to a text file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.dump(my_obj, f)
