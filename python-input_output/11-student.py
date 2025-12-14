#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary of the Student instance.

        If attrs is a list of strings, only attributes listed in attrs
        that exist in the instance are returned.
        Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list):
            result = {}
            for attr in attrs:
                if isinstance(attr, str) and hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result

        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
        using the provided dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
