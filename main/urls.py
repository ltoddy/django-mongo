from django.urls import path, include

urlpatterns = [
    path('mongo/', include('mongo.urls'), name='mongo'),
]
