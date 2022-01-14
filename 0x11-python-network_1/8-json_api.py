#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) == 2:
        req = requests.post(url, data={'q': argv[1]})
    else:
        req = requests.post(url, data={'q': ""})
    try:
        obj_js = req.json()
        if obj_js:
            print("[{}] {}".format(obj_js.get("id"), obj_js.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
