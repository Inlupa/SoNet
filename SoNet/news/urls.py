from django.urls import path
from .views import *
urlpatterns = [
    path('news', news_mainpage, name='new_mainpage'),
]