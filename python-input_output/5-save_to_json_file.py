#!/usr/bin/python3
"""Defines a function that saves an object to a file in JSON format."""


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using a JSON representation."""
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
