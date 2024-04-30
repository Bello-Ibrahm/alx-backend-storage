#!/usr/bin/env python3
"""
Python module that returns the list of
school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Find by topic
    """
    return mongo_collection.find({"topics": topic})
