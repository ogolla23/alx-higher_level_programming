#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)

    if r.status_code == requests.code.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
