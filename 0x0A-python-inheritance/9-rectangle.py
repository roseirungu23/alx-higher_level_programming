#!/usr/bin/python3
"""
Defines class BaseGeometry
"""


class BaseGeometry:
    """writes class BaseGeometry"""
    def area(self):
        """raise an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes class Rectangle"""
        self.__width = 0
        self.integer_validator("width", width)
        self.__width = width
        self.__height = 0
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
