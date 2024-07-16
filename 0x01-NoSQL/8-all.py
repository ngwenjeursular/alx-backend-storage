#!/usr/bin/env python3
""" MongoDB Operations with Python using pymongo """


def list_all(mongo_collection):
    """
    List all documents in the given MongoDB collection.

    Args:
        mongo_collection: pymongo collection object.

    Returns:
        A list of documents in the collection.
        Returns an empty list if no documents are found.
    """
    documents = mongo_collection.find()

    if documents.count() == 0:
        return []

    return documents
