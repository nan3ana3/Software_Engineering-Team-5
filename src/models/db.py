import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://yunjoo:1234@cluster0.iw1jtaf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cluster["software_engineering"]
#collection = db["test"]


def init_db(app):
    cluster.init_app(app)