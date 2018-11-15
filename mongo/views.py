from pprint import pprint
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import mongo_client


def index(request: HttpRequest) -> HttpResponse:
    database_names = {name: mongo_client[name].list_collection_names() for name in mongo_client.list_database_names()}
    pprint(database_names)
    # This return statement is only for the convenience of my development.
    return render(request, 'mongo/index.html', {'database_names': database_names})
    # return render(request, 'mongo/index.html', locals())
