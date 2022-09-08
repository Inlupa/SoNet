from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path(
        "",
        homepage.as_view(template_name= "mainpage/mainpage.html"),
        name="home",
    ),
    path(
        "<int:page>",
        views.listing,
        name="news-by-page"
    ),
    path(
        ".json",
        views.listing_api,
        name="news-api"
    ),

]