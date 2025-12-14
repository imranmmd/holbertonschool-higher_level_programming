#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")
