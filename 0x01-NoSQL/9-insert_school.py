#!/usr/bin/env python3
""" 9-insert_school module """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on **kwargs
    """
    # insert the documents into the collection
    result = mongo_collection.insert_one(kwargs)

    return result.inserted_id