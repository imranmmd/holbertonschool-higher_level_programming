#!/usr/bin/env python3
"""Module for serializing and deserializing CustomObject using pickle."""

import pickle


class CustomObject:
    """Defines a custom object that can be serialized with pickle."""

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current object and save it to a file.

        Args:
            filename (str): The file where the object will be saved.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject from a file.

        Args:
            filename (str): The file to load the object from.

        Returns:
            CustomObject or None: The deserialized object or None on failure.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None

        return None
