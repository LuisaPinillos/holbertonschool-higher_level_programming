#!/usr/bin/python3
"""
Script that takes in a URL, sends a request
to the URL and displays the body of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    req = requests.get(argv[1])
    if int(req.status_code) < 400:
        print(req.text)
    else:
        print("Error code: {}". format(req.status_code))
