from django.urls import path

from . import views

urlpatterns = [
    path(r'signup/', views.SignUpUser.as_view(), name='signup'),
    path(r'signin/', views.LoginUser.as_view(), name='signin'),
    path(r'logout/', views.logout_user, name='logout'),
]
