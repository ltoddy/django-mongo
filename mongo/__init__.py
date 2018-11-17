from django.http import Http404
from pymongo import MongoClient

from mongo.config import config

try:
    mongo_client = MongoClient(config['development']().mongo_uri())
except:
    raise Http404
