from django.test import TestCase
from pymongo import MongoClient

from ..config import config
from ..utils import get_database_names


class UtilTests(TestCase):
    def setUp(self):
        self.client = MongoClient(config['testing']().mongo_uri())
        self.database_names = self.client.list_database_names()

    def test_database_names(self):
        database_names = list(get_database_names(self.client).keys())
        self.assertListEqual(self.database_names, database_names)

    def test_collection_names(self):
        collection_names = list(get_database_names(self.client).values())
        names = []
        for db in self.database_names:
            names.append(self.client[db].list_collection_names())
        self.assertListEqual(names, collection_names)
