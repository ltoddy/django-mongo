from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('mongo/', include('mongo.urls'), name='mongo'),
    path('admin/', admin.site.urls)
]
