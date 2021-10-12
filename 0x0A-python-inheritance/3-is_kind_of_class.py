#!/usr/bin/python3
"""
Function that returns True if the object is
an instance of a class that inherited class
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """
    object is a type a_class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
