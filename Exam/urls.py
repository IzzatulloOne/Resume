from django.urls import path
from . import views
from ForExam import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='index page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)