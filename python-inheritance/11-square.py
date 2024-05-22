#!/usr/bin/python3
"""
This module defines a class Square
that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class used to represent a Square,
    inherits from Rectangle.
    """
    def __init__(self, size):
        """
        Initialize the square with a size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return a string representation
        of the square.

        Returns:
            str: A string representing the
            square in the format [Square] <width>/<height>.
        """
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
