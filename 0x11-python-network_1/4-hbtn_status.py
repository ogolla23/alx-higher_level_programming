#!/usr/bin/python3
"""A script that fetches a url"""
import requests
def main():
    """
    A function that fetches url
    """
    url = 'https://alx-intranet.hbtn.io/status'
    req = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(req.text)))
    print("\t- content: {}".format(req.text))
if __name__ == "__main__":
    main()
