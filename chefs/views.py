import re
from django.shortcuts import render
from .models import Chefs

# Create your views here.

def ChefsIntroduction(request):
    chefs = Chefs.objects.all().order_by('-id')[0:3]

    return render(
        request=request,
        template_name= "chefs.html",
        context={
            'chefs': chefs
        }
    )