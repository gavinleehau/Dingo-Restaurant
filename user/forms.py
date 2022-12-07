from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, Select, FileInput
from django.forms import ModelForm, models, widgets,Form
from django.core.exceptions import ValidationError


class RegisterForm(UserCreationForm):
    fullname = forms.CharField(max_length=100, help_text='Họ và tên', label= 'Họ và tên:')
    email = forms.CharField(max_length=100, help_text='Email', label= 'Email:')
    phoneNumber = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'fullname', 'email', 'phoneNumber', 'password1', 'password2']