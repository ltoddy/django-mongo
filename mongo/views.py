from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import mongo_client


def index(request: HttpRequest) -> HttpResponse:
    database_names = mongo_client.list_database_names()
    return render(request, 'mongo/index.html', {'database_names': database_names})
