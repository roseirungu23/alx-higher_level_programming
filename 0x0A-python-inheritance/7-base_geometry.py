#!/usr/bin/python3
"""
Defines class BaseGeometry
"""


class BaseGeometry:
    """writes class BaseGeometry with public instance area"""
    def area(self):
        """raises an exceptiion when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates the value"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
