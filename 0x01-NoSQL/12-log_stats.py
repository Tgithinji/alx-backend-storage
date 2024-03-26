#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


if __name__ == '__main__':
    """
    Provide some stats about Nginx logs stored in MongoDB
    """
    client = client = MongoClient('mongodb://127.0.0.1:27017')
    mongo_collection = client.logs.nginx

    # count the number of documents in this collection
    document_count = mongo_collection.count_documents({})
    print('{} logs'.format(document_count))

    # count the documents with specific methods
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        count = mongo_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, count))

    status_check = mongo_collection.count_documents({
        'method': 'GET',
        'path': '/status'
        })
    print('{} status check'.format(status_check))
