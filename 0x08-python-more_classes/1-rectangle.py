#!/usr/bin/python3
"""Define a empty Rectangle"""


class Rectangle:
    """Square has a width"""

    @property
    def height(self):
        """to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set it"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, width=0, height=0):
        """width and height initialization"""
        self.height = height
        self.width = width
