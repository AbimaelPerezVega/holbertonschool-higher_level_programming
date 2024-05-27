#!/usr/bin/python3
"""
This module provides a function to
convert an object to its JSON string representation.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj (any): The object to serialize to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
