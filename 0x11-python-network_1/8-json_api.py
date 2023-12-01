#!/usr/bin/python3
"""
A script that sends a post request to a url
"""
from sys import argv
import requests


if __name__ == "__main__":
    letter = "" if len(argv) == 1 else argv[1]
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, {"letter": letter})

    try:
        result = req.json()
        if bool(result) is  false:
            print("No result")
        else:
            print("[{}] {}".format(result['id'], result['name']))
    except:
            print("Not a valid JSON")

