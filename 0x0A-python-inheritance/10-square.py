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


class Square(Rectangle):
    """Square representation"""
    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2
