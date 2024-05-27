#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """
    A class to represent a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute
        names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Args:
            attrs (list, optional): List of attribute names
            to retrieve. Defaults to None.

        Returns:
            dict: A dictionary representation of the student.
        """
        if attrs is not None and isinstance(attrs, list):
            return {key: getattr(self, key)
                    for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        using a dictionary.

        Args:
            json (dict): A dictionary to update the
            instance attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
