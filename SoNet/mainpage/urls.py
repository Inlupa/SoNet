from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='home'),
    # path('repair/', repair),
    # path('looks/', looks),
    # path('tech/', tech),
]