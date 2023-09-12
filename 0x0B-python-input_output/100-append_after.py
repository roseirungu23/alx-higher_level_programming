#!/usr/bin/python3
"""
Defines function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    text = ""
    with open(filename) as file:
        for line in file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as ofile:
        ofile.write(text)
