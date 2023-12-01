#!/usr/bin/python3
"""
A script that POST request a url
"""
import requests
from sys import argv


def main(argv):
    """
    A function that post request a url
    """
    url = argv[1]
    value = {"email": argv[2]}
    req = requests.post(url, data=value)

    print(req.text)


if __name__ == "__main__":
    main(argv)
