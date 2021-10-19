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
        """
        init contructor
        """

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
        elif value <= 0:
            raise ValueError("width must be > 0")

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
        elif value <= 0:
            raise ValueError("height must be > 0")

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
        self.__y = value

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def display(self):
        """print the rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            for a in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print("")

    def update(self, *args):
        """add the arguments to the attributes"""
        for x in range(len(args)):
            if x == 0:
                self.id = args[x]
            if x == 1:
                self.__width = args[x]
            if x == 2:
                self.__height = args[x]
            if x == 3:
                self.__x = args[x]
            if x == 4:
                self.__y = args[x]

    def __str__(self):
        """return a string"""
        return(f"[Rectangle] \
({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}")
