from django.urls import path
from django.views.decorators.cache import cache_page

from . import views


urlpatterns = [
    path('', cache_page(60)(views.HomePage.as_view()), name='index'),
    path(r'json/', views.get_json_view, name='json'),
    path(r'about/', views.SomeView.as_view(), name='about'),
    path(r'chat/', views.GuestChatView.as_view(), name='chat'),
    path(r'chat/<int:message_id>', views.get_message_view, name='message_inf'),
    path(r'chat/<slug:message_slug>', views.get_author_view, name='author_inf'),

]