from django.urls import path
from .views import *
urlpatterns = [
    path('offer/internet+tv', internet_tv, name='internet+tv'),
    path('offer/internet', internet, name='internet'),
    path('offer/tv', tv, name='tv'),
    # path('offer/internet+tv', get_data, name='get_data'),
    path('offer/hosting', hosting, name='hosting'),
]