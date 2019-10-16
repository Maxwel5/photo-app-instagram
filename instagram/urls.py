from django.urls import path
from . import views

urlpatterns = [
    path('',views.image, name = 'image'),
    path('search/', views.search_results, name='search_results')
]