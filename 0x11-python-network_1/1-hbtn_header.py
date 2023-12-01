#!/usr/bin/python3
"""
A script that displays the x-Request-id value
in its header
"""
from sys import argv
from urllib.request import Request, urlopen


def main(argv):
    """
    A function that displays the value of
    the x-Request-id
    """
    url = argv
    request = Request(url)
    with urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))


if __name__ == "__main__":
    main(argv[1])
