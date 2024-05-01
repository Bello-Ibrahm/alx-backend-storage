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


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Comments
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


def run():
    '''Provides stats about Nginx logs stored in MongoDB.
    '''
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)


if __name__ == "__main__":
    run()
