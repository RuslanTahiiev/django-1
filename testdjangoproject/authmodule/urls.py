from django.urls import path

from . import views

urlpatterns = [
    path('signup', views.SignUpUser.as_view(), name='signup'),
]
