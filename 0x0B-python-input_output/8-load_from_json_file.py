#!/usr/bin/python3
""" contains the module load from json file function """
import json


def load_from_json_file(filename):
    """ creates an obj of a  json file """
    with open(filename, encoding='utf-8') as f:
        return json.load(f)
