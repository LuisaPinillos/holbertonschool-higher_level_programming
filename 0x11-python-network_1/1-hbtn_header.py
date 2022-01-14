#!/usr/bin/python3
"""
Script that sends a request to the URL and
displays the value of the X-Request-Id.
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        html = response.headers
        print(html["X-Request-Id"])
