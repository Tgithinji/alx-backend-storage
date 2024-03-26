#!/usr/bin/env python3
"""
8-all module
"""


def list_all(mongo_collection):
    """
    Lists all documents in a collection
    """
    list_docs = []

    for doc in mongo_collection.find():
        list_docs.append(doc)

    return list_docs
