"""etl.py

Implementes `transform`
We are going to do the `Transform` step of an Extract-Transform-Load.
"""


def transform(legacy_data: dict) -> dict:
    """transform

    to transform the legacy data format to the shiny new format
    like a following.

    e.g.)
        legacy_data = {1: ["A", "E", "I", "O", "U"]}
        data = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}

    Args:
        legacy_data (dict): dict

    Returns:
        dict: new dict using given structure
    """
    result = {}

    for key, value in legacy_data.items():
        for ch in value:
            result[ch.lower()] = key

    return result
