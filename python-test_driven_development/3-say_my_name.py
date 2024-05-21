#!/usr/bin/python3
"""
This module provides a function to print a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>

    Parameters:
    first_name: string representing the first name
    last_name: string representing the last name (optional)

    Raises:
    TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
