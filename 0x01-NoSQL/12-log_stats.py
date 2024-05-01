#!/usr/bin/env python3
"""
Python module that provides some stats about Nginx logs stored in MongoDB

Database: logs
Collection: nginx
Display (same as the example):
    first line: x logs, x number of documents in this collection
    second line: Methods
    5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    one line with number of documents with:
        method=GET
        path=/status
"""
from pymongo import MongoClient


def log_stats(mongo_collection):
    """Prints stats about nginx request logs.
    """
    print('{} logs'.format(mongo_collection.count_documents({})))
    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        req_count = len(list(mongo_collection.find({'method': method})))
        print('\tmethod {}: {}'.format(method, req_count))
    status_checks_count = len(list(
        mongo_collection.find({'method': 'GET', 'path': '/status'})
    ))
    print('{} status check'.format(status_checks_count))


def run():
    '''Provides stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    log_stats(client.logs.nginx)


if __name__ == "__main__":
    run()
