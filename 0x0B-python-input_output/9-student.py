#!/usr/bin/python3
"""
Defines a clas student
"""


class Student:
    """Representation of class student"""
    def __init__(self, first_name, last_name, age):
        """initilizes class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = Age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
