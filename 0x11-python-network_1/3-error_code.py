#!/usr/bin/python3
"""
Script that sends a request to the URL
and displays the body of the response.
"""

from urllib import request
from urllib import error
from sys import argv

if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            html = response.read()
        print(html.decode('utf8'))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
