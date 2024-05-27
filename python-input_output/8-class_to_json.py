#!/usr/bin/python3
"""
Module that provides a function to
convert an object's attributes to a dictionary.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with
    simple data structure (list, dictionary,
    string, integer, and boolean) for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary representation of the instance attributes.
    """
    return obj.__dict__
