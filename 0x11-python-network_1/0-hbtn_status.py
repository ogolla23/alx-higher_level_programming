#!/usr/bin/python3
"""This is a python script that fetches a url"""
from urllib.request import Request, urlopen

def main():
    """ A function that prints the url"""
    req = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(req) as response:
        HTML = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(HTML)))
        print("\t- content: {}".format(HTML))
        print("\t- utf8 content: {}".format(HTML.decode("utf-8")))

if __name__ == "__main__":
    main()
