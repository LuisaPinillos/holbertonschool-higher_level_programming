#!/usr/bin/python3
"""
The class Square that inherits from
Rectangle. Call the super class with
id, x, y, width and height
"""


from models.rectangle import Rectangle
"""
Import the Rectangle class
"""


class Square(Rectangle):
    """Square class inherits Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        init contructor
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return a string"""
        return(f"[Square] \
({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """to retrieve it"""
        return self.width

    @size.setter
    def size(self, value):
        """to set it"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
