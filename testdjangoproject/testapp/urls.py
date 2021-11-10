from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'json', views.get_json_view, name='json'),
    path(r'about', views.get_some_view, name='json'),
    path(r'chat', views.guest_chat_view, name='json'),
]