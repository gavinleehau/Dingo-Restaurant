from django.http import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('chefs/', views.chefs, name='chefs'),
]