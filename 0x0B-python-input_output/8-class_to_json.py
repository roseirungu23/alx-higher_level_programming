#!/usr/bin/python3
"""
Defines function class-to-json
"""


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    if isinstance(obj, dict):
        return obj
    elif isinstance(obj, list):
        return [class_to_json(item) for item in obj]
    elif isinstance(obj, bool) or isinstance(obj, int) or isinstance(obj, str):
        return obj
    elif isinstance(obj, object):
        obj_dict = {}
        for key, value in vars(obj).items():
            obj_dict[key] = class_to_json(value)
        return obj_dict
    else:
        return None
