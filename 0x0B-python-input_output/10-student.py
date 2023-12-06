#!/usr/bin/python3
"""Student modle."""


class Student():
    """Defines a Student."""

    def __init__(self, first_name, last_name, age):
        """Sets the necessary attributes for the Student object.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is not None:
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
