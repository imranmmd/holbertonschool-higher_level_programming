#!/usr/bin/python3
"""Defines a function that loads an object from a JSON file."""


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    import json
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
