from django.shortcuts import render, get_object_or_404
from .models import Special, Breakfast, Lunch, Dinner
from contact.models import ContactInfo

# Create your views here.

def menu(request):
    special = Special.objects.all().order_by('-id')
    breakfast = Breakfast.objects.all().order_by('-id')
    lunch = Lunch.objects.all().order_by('-id')
    dinner = Dinner.objects.all().order_by('-id')
    contactInfo = ContactInfo.objects.get(pk=1)
    
    return render(
        request=request,
        template_name = "menu.html",
        context={
            'special': special,
            'breakfast': breakfast,
            'lunch': lunch,
            'dinner': dinner,
            'contactInfo': contactInfo,
        }
    )