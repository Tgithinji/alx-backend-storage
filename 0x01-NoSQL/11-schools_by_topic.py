#!/usr/bin/env python3
""" 11-schools_by_topic """


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of schools having a specific topic
    """
    schools = [doc for doc in mongo_collection.find({'topics': topic})]
    return schools
