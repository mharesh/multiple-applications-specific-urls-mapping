app_name='string'
from django.urls import path
from app.views import *


urlpatterns=[
    path('index/',index,name='index'),
    path('new/',new,name='new'),
]