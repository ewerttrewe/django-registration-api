from django.contrib import admin
from django.urls import path
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.development.DEBUG:
    urlpatterns += static(settings.development.STATIC_URL, document_root=settings.development.STATIC_ROOT)
    urlpatterns += static(settings.development.MEDIA_URL, document_root=settings.development.MEDIA_ROOT)