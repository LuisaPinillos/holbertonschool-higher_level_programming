#!/usr/bin/python3
"""
Function that returns True if the object
is an instance of a class that inherited
(directly or indirectly) otherwise False.
"""


def inherits_from(obj, a_class):
    """
    object and type a_class
    """
    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
