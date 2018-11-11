from pymongo import MongoClient

from mongo.config import Config

mongo_client = MongoClient(Config().mongo_uri())
