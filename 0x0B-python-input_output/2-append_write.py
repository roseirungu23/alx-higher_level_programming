#!/usr/bbin/python3
"""
Defines function append_write
"""


def append_write(filename="", text=""):
    """ appends a string at the end of a text file (UTF8)
    returns the number of characters added"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
