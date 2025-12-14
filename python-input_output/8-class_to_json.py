#!/usr/bin/python3
"""Defines a function that returns a dict of an object."""


def class_to_json(obj):
    """Return the dictionary  object for JSON serialization."""
    return obj.__dict__
