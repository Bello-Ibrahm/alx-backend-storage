#!/usr/bin/env python3
"""
Python module that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    list all collections
    """
    if not mongo_collection:
        return []
    return list(mongo_collection.find())
