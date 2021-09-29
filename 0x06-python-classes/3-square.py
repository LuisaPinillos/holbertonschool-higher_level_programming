#!/usr/bin/python3
"""Class Square"""


class Square:
    """Square has a size"""

    def __init__(self, size=0):
        """This class raise error"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Return the square area"""
        return self.__size ** 2
