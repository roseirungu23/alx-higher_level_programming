#!/usr/bin/python3
"""
Defines a function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as a file:
        json.dump(my_obj, file)
