from django.shortcuts import render

# Create your views here.

def Order(request):

    return render(
        request=request,
        template_name= "cart.html",
        context={}
    )