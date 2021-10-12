#!/usr/bin/python3
import json
"""
Function that returns the
JSON representation of an
object (string).
"""


def to_json_string(my_obj):
    """
    my_object is a string
    """
    return json.dumps(my_obj)
