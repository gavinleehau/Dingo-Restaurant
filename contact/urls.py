from django.http import HttpResponse
from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.contact, name='contact'),
	path('success',views.success_page, name='success_page'),
]