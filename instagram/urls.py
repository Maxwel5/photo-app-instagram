from django.urls import path
from django.contrib.auth import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.image, name = 'image'),
    path('search/', views.search_results, name='search_results'),
    path('allImages/',views.index,name ='display-images'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
