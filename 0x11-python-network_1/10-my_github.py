#!/usr/bin/python3
"""script that takes your Github credentials"""
import sys
import requests

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    try:
        r = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
        print(r.json()['id'])
    except KeyError:
        print("None")
