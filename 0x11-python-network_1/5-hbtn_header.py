#!/usr/bin/python3
"""sends a request to url and displays the value of the variable X-Request-Id"""

import requests
import sys


def main():
    """ main function"""
    url = str(sys.argv[1])
    r = requests.get(url)
    content = r.headers.get('X-Request-Id')
    print(content)


if __name__ == "__main__":
    main()
