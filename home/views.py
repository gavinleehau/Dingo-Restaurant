from django.shortcuts import render, redirect
from blog.models import blog
from chefs.models import Chefs
from aboutUs.models import History, Feedback
from contact.models import ContactInfo, Reservations
from menu.models import Special, Breakfast, Lunch, Dinner

# Create your views here.

def home(request):
    data = Reservations()
    if request.method == 'POST':
        data.email = request.POST['email']
        data.customerName = request.POST['customerName']
        data.phoneNumber = request.POST['phoneNumber']
        data.date = request.POST['date']
        data.time = request.POST['time']
        data.amount = request.POST['amount']
        data.note = request.POST['note']
        data.save()
        return redirect('success_page')

    latestPosts = blog.objects.all().order_by('-id')[0:3]
    chefs 		= Chefs.objects.all().order_by('-id')[0:3]
    ourHistory  = History.objects.all()
    feedback    = Feedback.objects.all().order_by('-id')[0:5]
    contactInfo = ContactInfo.objects.get(pk=1)

    special = Special.objects.all().order_by('-id')[0:6]
    breakfast = Breakfast.objects.all().order_by('-id')[0:6]
    lunch = Lunch.objects.all().order_by('-id')[0:6]
    dinner = Dinner.objects.all().order_by('-id')[0:6]
    ExclusiveItems = Special.objects.all().order_by('-id')[0:3]
    
    return render(
        request=request,
        template_name = "home.html",
        context={
            'latestPosts': latestPosts,
            'chefs': chefs,
            'ourHistory': ourHistory,
            'feedback': feedback,
            'contactInfo': contactInfo,
            'special': special,
            'breakfast': breakfast,
            'lunch': lunch,
            'dinner': dinner,
            'ExclusiveItems': ExclusiveItems,
        }
    )