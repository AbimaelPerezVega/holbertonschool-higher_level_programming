#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    
    a: first number, must be an integer or float
    b: second number, must be an integer or float, default is 98

    Returns the sum of a and b, both casted to integers if they are floats.
    Raises a TypeError if either a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)
