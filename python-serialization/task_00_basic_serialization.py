#!/usr/bin/env python3
"""Basic serialization module for saving and loading JSON data."""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): The output JSON file name.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file into a Python dictionary.

    Args:
        filename (str): The input JSON file name.

    Returns:
        dict: The deserialized JSON data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
