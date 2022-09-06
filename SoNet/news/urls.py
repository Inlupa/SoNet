from django.urls import path
from .views import *
urlpatterns = [
    path('search_article/display/', news_mainpage, name='new_mainpage'),
]