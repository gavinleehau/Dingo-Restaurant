from django.http import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.menu, name='menu'),
	path('slug:category_slug', views.menu, name='food_by_category')
]