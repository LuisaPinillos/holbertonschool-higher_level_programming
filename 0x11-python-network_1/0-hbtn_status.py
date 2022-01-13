#!/usr/bin/python3
# Write a Python script that fetches.
import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
   html = response.read()
