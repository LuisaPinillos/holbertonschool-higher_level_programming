#!/usr/bin/python3
"""
function that add
two integers and return
the result.
"""


def add_integer(a, b=98):
    """
    add the integer a and the integer b
    if is float convert to integer.
    """

    if type(a) is float:
        a = int(a)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
