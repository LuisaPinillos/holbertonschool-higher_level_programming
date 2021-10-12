#!/usr/bin/python3
"""
Function that returns the list
of available attributes and
methods of an object.
"""


def lookup(obj):
    """obj is the object for return its
    methods and attributes."""
    return dir(obj)
