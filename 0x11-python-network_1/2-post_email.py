#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request.
"""
from sys import argv
from urllib.parse import urlencode
from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    r = Request(url, data)

    with urlopen(r) as response:
        print(response.read().decode("utf-8", "replace"))
