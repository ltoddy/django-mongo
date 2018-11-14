from django.http import Http404
from pymongo import MongoClient

from mongo.config import Config

try:
    mongo_client = MongoClient(Config().mongo_uri())
except:
    raise Http404
