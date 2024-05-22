#!/usr/bin/python3
"""
This module defines a class BaseGeometry.
"""


class BaseGeometry:
    """
    A class named BaseGeometry.
    """
    def area(self):
        """
        Public instance method that
        raises an exception indicating that
        the method is not implemented.
        """
        raise Exception("area() is not implemented")
