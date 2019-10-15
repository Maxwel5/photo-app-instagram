from django.conf.urls import url
from . import views

urlpatterns = [
    path('',views.instagram, name = 'instagram'),
]