from django.shortcuts import render, get_object_or_404
from .models import Food
from contact.models import ContactInfo

# Create your views here.

def menu(request):
    foods = Food.objects.all().order_by('-id')
    contactInfo = ContactInfo.objects.get(pk=1)
    
    return render(
        request=request,
        template_name = "menu.html",
        context={
            'foods': foods,
            'contactInfo': contactInfo,
        }
    )