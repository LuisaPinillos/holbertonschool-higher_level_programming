#!/usr/bin/python3
"""
Create
a empty
class
"""


class BaseGeometry():
    """
    Empty class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if isinstance(self.value, int) is False:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
