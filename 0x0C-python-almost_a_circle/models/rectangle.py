#!/usr/bin/python3
"""
The class Rectangle that inherits from Base
Private instance attributes, each with its
own public getter and setter
"""


from models.base import Base
"""
Import the base class
"""


class Rectangle(Base):
    """Rectangle class inherits Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return self"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it"""
        self.__width = value

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")

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
    def x(self):
        """to retrieve it"""
        return self.__x

    @x.setter
    def x(self, value):
        """to set it"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """to retrieve it"""
        return self.__y

    @y.setter
    def y(self, value):
        """to set it"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__x = value