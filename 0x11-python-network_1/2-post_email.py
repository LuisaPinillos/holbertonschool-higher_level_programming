#!/usr/bin/python3
"""
Script that  sends a POST request to the
passed URL with the email as a parameter.
"""

from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    getemail = {}
    getemail["email"] = argv[2]
    data = parse.urlencode(getemail)
    data = data.encode('ascii')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        html = response.read()
    print(html.decode('utf8'))
