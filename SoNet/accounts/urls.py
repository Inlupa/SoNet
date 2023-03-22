from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register , name="register"),
    path('logout/', user_logout, name="logout"),
    path('profile/', profile_page, name="profile_page"),
    path('password/', change_password, name='change_password'),
    path('profile_change/', profile_change, name='profile_change'),
    ]