from cmath import phase
import email
from statistics import mode
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

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
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser


class Staff(models.Model):
    GENDER = (
        (0,"Nam"),
        (1,"Nữ")
    )

    STATUS = (
        (0,"Hoạt động"),
        (1,"Không hoạt động")
    )

    name = models.CharField('Tên Nhân viên:', max_length=100)
    age = models.CharField('Tuổi:', max_length=100, default='')
    avatar = models.ImageField(verbose_name=_("Ảnh nhân viên"), default='')
    email = models.CharField('Email Nhân viên:', max_length=200)
    phone = models.CharField('Số điện thoại',blank=False, max_length=20)
    BirthDate = models.DateField('Ngày sinh')
    gender = models.IntegerField('Giới tính', choices=GENDER, default=0)
    citizenshipCard = models.CharField('Số thẻ CCCD/CMND:', max_length=100)
    homeTown = models.CharField('Quê quán:', max_length=100)
    joinedDate = models.DateField('Ngày vào làm')
    status = models.IntegerField('Trạng thái', choices=STATUS, default=0)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="50px";/>'.format(self.avatar.url))
    image_tag.short_description='Image'

    class Meta:
        verbose_name = _("Nhân viên")
        verbose_name_plural = _("Nhân viên")

    def __str__(self):
        return self.name

    
