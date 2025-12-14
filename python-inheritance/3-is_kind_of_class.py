#!/usr/bin/python3
"""Defines a function to check instance or inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass.
    Otherwise, return False.
    """
    return isinstance(obj, a_class)
