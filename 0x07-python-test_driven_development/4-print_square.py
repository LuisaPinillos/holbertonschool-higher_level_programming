#!/usr/bin/python3
"""
function that prints a square
the size of that square must be a
integer.
"""


def print_square(size):
    """
    Size must be a integer and >= 0
    in otherwise raise a error.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not int and size < 0:
        raise TypeError("size must be an integer")
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print(" ")
