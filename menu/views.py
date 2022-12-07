from django.shortcuts import render, get_object_or_404
from .models import Special, Breakfast, Lunch, Dinner

# Create your views here.

def menu(request):
    special = Special.objects.all()
    breakfast = Breakfast.objects.all()
    lunch = Lunch.objects.all()
    dinner = Dinner.objects.all()
    
    return render(
        request=request,
        template_name = "menu.html",
        context={
            'special': special,
            'breakfast': breakfast,
            'lunch': lunch,
            'dinner': dinner,
        }
    )