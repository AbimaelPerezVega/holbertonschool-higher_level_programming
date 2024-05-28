#!/usr/bin/python3
"""
This module provides a function to
load an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        any: The object loaded from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

