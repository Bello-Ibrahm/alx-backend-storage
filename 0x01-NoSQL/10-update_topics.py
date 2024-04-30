#!/usr/bin/env python3
"""
Python module that changes all topics of a
school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """
    update many rows
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
