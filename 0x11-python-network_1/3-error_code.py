#!/usr/bin/python3
"""
A script that displays the body of a Response
"""
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def main(argv):
    """
    A function that manage urllib.error.HTTPError exceptions and
    print: Error code: followed by the HTTP status code
    """
    url = argv[1]
    req = Request(url)
    try:
        with urlopen(req)as response:
            print(response.read().decode9"ascii"))
    except HTTPError as  e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    main(argv)
