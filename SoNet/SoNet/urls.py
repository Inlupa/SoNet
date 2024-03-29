from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('mainpage.urls')),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('news.urls')),
    path('', include('offer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)