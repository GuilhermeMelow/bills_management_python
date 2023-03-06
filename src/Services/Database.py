from pymongo import MongoClient


def get_database():
    client = MongoClient(
        host='localhost',
        port=27017,
        uuidRepresentation='standard')

    return client.get_database("bills_database")
