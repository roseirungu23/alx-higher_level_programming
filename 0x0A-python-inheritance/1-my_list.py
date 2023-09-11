#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """Child class of class list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list in ascending order"""
        print(sorted(self))
