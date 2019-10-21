from django.urls import path
from django.contrib.auth import views
from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name = 'home'),
    path('search/', views.search_results, name='search_results'),
    path('allImages/',views.index,name ='display-images'),
    path('<int:image>/like/', views.likePost, name='likePost'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
