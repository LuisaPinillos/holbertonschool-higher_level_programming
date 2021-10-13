#!/usr/bin/python3
""" 
Function that returns the dictionary description
with simple data structure (list, dictionary, string, integer
and boolean) for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Class are serializable
    """
    return obj.__dict__
