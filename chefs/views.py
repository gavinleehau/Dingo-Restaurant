import re
from django.shortcuts import render
from .models import Chefs
from contact.models import ContactInfo

# Create your views here.

def ChefsIntroduction(request):
    chefs = Chefs.objects.all().order_by('-id')[0:3]
    contactInfo = ContactInfo.objects.get(pk=1)

    return render(
        request=request,
        template_name= "chefs.html",
        context={
            'chefs': chefs,
            'contactInfo': contactInfo,
        }
    )