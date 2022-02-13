import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get("DB_HOST")
port = int(os.environ.get("DB_PORT"))
dbName = os.environ.get("DB_NAME")

client = pymongo.MongoClient(host, port)
db = client[dbName]
collection = db["products"]


def getProducts():
    return collection.find()


def insertProduct(val):
    return collection.insert_one(val)
