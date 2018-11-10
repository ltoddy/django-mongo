from django.urls import path

from . import views

app_name = 'mongo'
urlpatterns = [
    path('', views.index, name='index')
]
