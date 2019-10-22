from django.urls import path
from django.contrib.auth import views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name = 'index'),
    path('search/', views.search_results, name='search_results'),
    path('like/(?P<image_id>[0-9]+)$',views.likePost, name='likePost'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='post_detail'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
