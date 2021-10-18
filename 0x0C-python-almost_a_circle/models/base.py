#!/usr/bin/python3
"""
Create a new class with a
private class attribute
__nb_objects
"""


class Base():
    """The Bass class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
