#!/usr/bin/python3
"""
function that
creates an Object from
a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Filename is a file
    """
    with open(filename, 'r', encoding='UTF8') as f:
        return json.load(f)
