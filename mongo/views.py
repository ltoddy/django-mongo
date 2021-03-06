import math
from pprint import pformat
from textwrap import shorten

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from pymongo import MongoClient

from . import mongo_client
from .utils import get_database_names
from .forms import LoginForm


def index(request: HttpRequest) -> HttpResponse:
    # database_names = {name: mongo_client[name].list_collection_names() for name in mongo_client.list_database_names()}
    database_names = get_database_names(mongo_client)
    return render(request, 'mongo/index.html', {'database_names': database_names})


def detail(request: HttpRequest, db_name: str, collection_name: str) -> HttpResponse:
    database_names = {name: mongo_client[name].list_collection_names() for name in mongo_client.list_database_names()}
    current_db = mongo_client[db_name]
    current_collection = current_db[collection_name]

    per_page = int(request.GET.get('per_page', 10))
    page = int(request.GET.get('page', 0))

    date_list = map(lambda date: {'compressed': shorten(str(date), width=120), 'origin': pformat(date)},
                    current_collection.find({}, limit=per_page, skip=page * per_page))

    total = math.ceil(current_collection.count() / per_page)
    return render(
        request, 'mongo/detail.html',
        {
            'database_names': database_names,
            'current_db': db_name,
            'current_collection': collection_name,
            'date_list': date_list,
            'per_page': per_page,
            'pages': range(total),
            'current_page': page,
            'prev_page': page - 1,
            'next_page': page + 1,
            'total_page': (total - 1),
        }
    )


def login(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mongo_config = form.save(commit=True)
            global mongo_client
            mongo_client = MongoClient(mongo_config.uri())
            return redirect(reverse('mongo:index'))
    else:
        form = LoginForm()
    return render(request, 'mongo/login.html', {'form': form})


def logout(request: HttpRequest) -> HttpResponse:
    # TODO
    return HttpResponse('这个页面用于退出你当前的mongo, 回到默认mongo的配置上')


def shell(request: HttpRequest) -> HttpResponse:
    return HttpResponse('mongo shell')
