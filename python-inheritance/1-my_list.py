#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """Custom list class with a method to print a sorted version."""

    def print_sorted(self):
        """Print the list sorted in ascending order and return it."""
        sorted_list = sorted(self)
        print(sorted_list)
        return sorted_list
