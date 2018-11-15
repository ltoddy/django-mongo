from django.urls import path

from . import views

app_name = 'mongo'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<str:db_name>/<str:collection_name>', views.detail, name='detail'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
