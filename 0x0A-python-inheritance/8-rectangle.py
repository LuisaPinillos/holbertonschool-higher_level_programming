#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Type class of Rectangle inherit BaseGeometry
    """

    def __init__(self, width, height):
        """
        Constructor Magic method
        """

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__heigh = height
