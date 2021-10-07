#!/usr/bin/python3
"""
function that prints a name
and the arguments must be
strings.
"""


def say_my_name(first_name, last_name=""):
    """
    First_name and last_name must be
    strings otherwise raise a error.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}" .format(first_name, last_name))
