from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from . import mongo_client


def index(request: HttpRequest) -> HttpResponse:
    database_names = {name: mongo_client[name].list_collection_names() for name in mongo_client.list_database_names()}
    return render(request, 'mongo/index.html', {'database_names': database_names})


def detail(request: HttpRequest, db_name: str, collection_name: str) -> HttpResponse:
    database_names = {name: mongo_client[name].list_collection_names() for name in mongo_client.list_database_names()}
    current_db = mongo_client[db_name]
    current_collection = current_db[collection_name]
    print('=============>', current_db.name)
    return render(
        request, 'mongo/detail.html',
        {'database_names': database_names, 'current_db': db_name, 'current_collection': collection_name}
    )


def login(request: HttpRequest) -> HttpResponse:
    # TODO
    return HttpResponse('这个页面用来更来 mongo 的 uri')


def logout(request: HttpRequest) -> HttpResponse:
    # TODO
    return HttpResponse('这个页面用于退出你当前的mongo, 回到默认mongo的配置上')
