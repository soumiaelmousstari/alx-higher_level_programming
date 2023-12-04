#!/usr/bin/python3
"""Module containing add_attribute method"""


def add_new_attribute(obj, name, value):
    """Method checking if attribute can be set and sets
    where possible"""
    if '__dict__' not in dir(obj) or \
       '__slots__' in dir(obj):
           raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
