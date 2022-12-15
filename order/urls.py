from django.http import HttpResponse
from django.urls import path, re_path, include
from . import views

urlpatterns = [
	path('', views.shopcart, name='order'),
	path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
]