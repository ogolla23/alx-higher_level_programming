#!/usr/bin/python3
"""
A script that displays the x-Request-id variable value
"""
import requests
from sys import argv

def main(argv):
    """
    A function that displays the x-Request-id
    variable value
    """
    url = argv[1]
    req = requests.get(url)
    print(req.headers.get("x-Request-Id"))

if __name__ == "__main__":
    main(argv)
