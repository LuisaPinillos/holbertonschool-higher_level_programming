#!/usr/bin/python3
"""Define a empty Rectangle"""


class Rectangle:
    """Square has a width"""

    def __init__(self, width=0, height=0):
        """width and height initialization"""
        self.height = height
        self.width = width

    @property
    def height(self):
        """to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set it"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter:"""
        if self.__width and self.__height == 0:
            return (0)
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        string1 = ""
        if self.__height and self.__width == 0:
            return string1
        else:
            for i in range(self.height):
                for j in range(self.width):
                    string1 += '#'
                if j != self.__width and i != self.__height:
                    if (i + 1) != self.__height:
                        string1 += '\n'
            return string1

    def __repr__(self):
        r = 'Rectangle(' + str(self.__width) + ', ' + str(self.__height) + ')'
        return r

    def __del__(self):
        print("Bye rectangle...")
