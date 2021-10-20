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
