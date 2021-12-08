import os

from pymongo import MongoClient


def get_db_collections():
    # point to the mongodb URI if it exists
    host = os.environ.get("MONGODB_URI", "mongodb://localhost:27017/Playlister")
    client = MongoClient(host=f"{host}?retryWrites=false")
    db = client.get_default_database()
    return db.playlists, db.comments
