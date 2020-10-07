#!/usr/bin/python3
""" contains the function of json string"""
import json


def from_json_string(my_str):
    """ returns object by json"""
    return json.loads(my_str)
