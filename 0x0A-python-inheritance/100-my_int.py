#!/usr/bin/python3
"""MyInt class module"""


class MyInt(int):
    """A MyInt class"""
    def __equal__(self, other):
        """Overides and inverts == operator"""
        return int(self) is not int(other)

    def __neequal__(self, other):
        """Overides and inverts != operator"""
        return int(self) is int(other)
