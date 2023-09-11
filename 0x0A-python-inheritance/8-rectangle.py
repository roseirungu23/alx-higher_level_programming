#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance  area and integer_validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes class Rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
