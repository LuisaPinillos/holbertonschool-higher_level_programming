#!/usr/bin/python3
"""
list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
Use the GITHUB API.
"""

import requests
from sys import argv

if __name__ == "__main__":
    rep = argv[1]
    user = argv[2]
    url = "https://api.github.com/repos/{}/{}".format(user, rep)
    url += 'commits?per_page=10'
    req = requests.get(url)
    for i in req.json():

        print("{}: {}".format(i.get("sha"
                                    ) i.get("commit"
                                            ).get("author"
                                                  ).get("name")))
