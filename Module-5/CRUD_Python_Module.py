# Example Python Code to Insert a Document

from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self):
        # Initializing the MongoClient. This helps to access the MongoDB
        # databases and collections. This is hard-wired to use the aac
        # database, the animals collection, and the aac user.
        #
        # You must edit the password below for your environment.
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'PASSWORD'   # CHANGE THIS
        HOST = 'localhost'
        PORT = 27017
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(
            'mongodb://%s:%s@%s:%d/?authSource=admin' % (USER, PASS, HOST, PORT)
        )
        self.database = self.client[DB]
        self.collection = self.database[COL]

 # -------------------------
    # CREATE
    # -------------------------
    def create(self, data):
        """
        Inserts a document into the MongoDB collection.
        Returns True if successful, otherwise False.
        """
        if data is not None and isinstance(data, dict):
            try:
                self.collection.insert_one(data)
                return True
            except Exception:
                return False
        return False

    # -------------------------
    # READ
    # -------------------------
    def read(self, query):
        """
        Queries documents from the MongoDB collection.
        Uses find() and returns results as a list.
        """
        try:
            cursor = self.collection.find(query)  # must use find()
            return list(cursor)
        except Exception:
            return []

    # -------------------------
    # UPDATE
    # -------------------------
    def update(self, query, update_data):
        """
        Updates documents in the MongoDB collection.
        Returns the number of documents modified.
        """
        if query is not None and update_data is not None:
            try:
                result = self.collection.update_many(
                    query,
                    {"$set": update_data}
                )
                return result.modified_count
            except Exception:
                return 0
        return 0

    # -------------------------
    # DELETE
    # -------------------------
    def delete(self, query):
        """
        Deletes documents from the MongoDB collection.
        Returns the number of documents deleted.
        """
        if query is not None:
            try:
                result = self.collection.delete_many(query)
                return result.deleted_count
            except Exception:
                return 0
        return 0
