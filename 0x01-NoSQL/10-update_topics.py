#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """
# 10-update_topics.py


def update_topics(mongo_collection, name, topics):
    """
    Update the topics of a school document based on its
    name in the MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.
        name: Name of the school to update (string).
        topics: List of topics approached in the school (list of strings).

    Returns:
        None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
