#!/usr/bin/python3
"""Class Square"""


class Square:
    """Square has a size"""

    @property
    def size(self):
        """to retrieve it"""
        return self.__size

    def my_print(self):
        i = 0
        j = 0
        self.prs = self.__size
        """prints in stdout the square with the character #"""
        if self.prs == 0:
            print("\n", end="")
        else:
            for i in range(0, self.prs):
                for j in range(0, self.prs):
                    print("#", end="")
                print("\n", end="")

    @size.setter
    def size(self, value):
        """to set it"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        """size initialization"""
        self.__size = size

    def area(self):
        """Return the square area"""
        return self.__size ** 2
