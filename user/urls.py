from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.Register, name='register'),
    path('login', views.Login, name='login' ),
    path('logout', auth_views.LogoutView.as_view(next_page="/"), name="logout"),
]