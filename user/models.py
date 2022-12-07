from cmath import phase
import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='')
    name = models.CharField('Tên khách hàng:', max_length=100)
    email = models.CharField('Email khách hàng:', max_length=200)
    phone = models.CharField('Số điện thoại',blank=False, max_length=20)

    class Meta:
        verbose_name = _("Khách hàng")
        verbose_name_plural = _("Khách hàng")

    def __str__(self):
        return self.name

    
