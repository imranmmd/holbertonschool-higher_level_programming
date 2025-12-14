#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a text file (UTF-8) and print its contents to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
