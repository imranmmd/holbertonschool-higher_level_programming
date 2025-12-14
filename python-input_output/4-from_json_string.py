#!/usr/bin/python3
"""Defines a function that returns object from a JSON string."""


def from_json_string(my_str):
    """Return the Python object represented by a JSON string."""
    import json
    return json.loads(my_str)
