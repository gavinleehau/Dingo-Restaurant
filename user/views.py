from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from user.forms import RegisterForm

from .models import UserProfile

# Create your views here.

def Login(request):
    message=""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            current_user = request.user
            userprofile = UserProfile.objects.get(user_id=current_user.id)
            return redirect('home')
        else:
            messages.info(request,"Tài khoản hoặc mật khẩu không đúng. Vui lòng thử lại")
        
    return render(
        request=request,
        template_name="login.html",
        context={
            'message': message
        }
    )

def Register(request):
    message=""
    if request.method =="POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            form.save() #completed sign up
            user = authenticate(username=username, password=password)
            login(request, user)


            #Create data in profile table for user
            
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.name = form.cleaned_data['fullname']
            data.email = form.cleaned_data['email']
            data.phone = form.cleaned_data['phoneNumber']
            data.save()
            messages.success(request, 'Tài khoản của bạn đã tạo thành công!') 
            return redirect('home')
        else:
            print('saiiiiiiiiii')
            messages.info(request, form.errors)

    return render(
        request=request,
        template_name="register.html",
        context={
            'message': message
        }
    )

