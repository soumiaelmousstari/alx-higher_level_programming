#!/usr/bin/python3
"""defining read_file function"""


def read_file(filename=""):
    """read filename with utf-8"""
    with open(filename, encoding="UTF-8") as f:
        print(f.read(), end="")
