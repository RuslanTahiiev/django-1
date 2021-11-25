from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path(r'json/', views.get_json_view, name='json'),
    path(r'about/', views.get_some_view, name='about'),
    path(r'chat/', views.guest_chat_view, name='chat'),
    path(r'chat/<int:message_id>', views.get_message_view, name='message_inf'),
    path(r'chat/<slug:message_slug>', views.get_author_view, name='author_inf'),

]