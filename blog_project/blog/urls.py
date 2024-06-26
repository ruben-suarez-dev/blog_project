from django.urls import path

from .views import *

urlpatterns = [
    path('api/post/get', get_all_post, name='get_all_post'),
    path('api/post/post', add_post, name='add_post'),
    path('api/post/<int:id>/get', filter_post_by_id, name='filter_post_by_id')
]