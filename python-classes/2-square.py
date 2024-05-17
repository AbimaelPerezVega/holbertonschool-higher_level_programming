#!/usr/bin/python3
"""
This module defines a class Square.
"""


class Square:
    """
    A class that defines a square by its size.
    """
    def __init__(self, size=0):
        """
        Initialize the square with a specific size.

        Args:
            size (int): The size of the square, must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
