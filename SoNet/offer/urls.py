from django.urls import path
from .views import *
urlpatterns = [
    path('offer/internet+tv', internet_tv, name='internet+tv'),
    path('offer/internet', internet, name='internet'),
    path('offer/tv', tv, name='tv'),
    path('offer/hosting', hosting, name='hosting'),
]