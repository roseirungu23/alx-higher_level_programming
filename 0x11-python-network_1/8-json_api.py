#!/usr/bin/python3
""" Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user"""

import sys
import requests


def main():
    """ main function"""
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
