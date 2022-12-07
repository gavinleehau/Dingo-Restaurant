from django.http import HttpResponse
from django.urls import path, re_path, include
from . import views

urlpatterns = [
	path('', views.ChefsIntroduction, name='chefs'),
]