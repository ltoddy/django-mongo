from typing import Dict, List

from pymongo import MongoClient


def get_database_names(client: MongoClient) -> Dict[str, List[str]]:
    database_names = {name: client[name].list_collection_names() for name in client.list_database_names()}
    return database_names
