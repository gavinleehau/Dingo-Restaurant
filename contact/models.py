from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class ContactInfo(models.Model):
    address        = models.CharField('Địa chỉ', max_length=100)
    phoneNumber    = models.CharField('Số điện thoại', max_length=11)
    email          = models.CharField('Email', null=True, max_length=100)
    coordinates    = models.TextField('Vị trí trên bản đồ', null=True)

    class Meta:
        verbose_name = _("Thông tin liên hệ")
        verbose_name_plural = _("Thông tin liên hệ")
    
    def __str__(self):
      	return self.address

class Reservations(models.Model):
    STATUS = (
        (0, 'Mới'),
        (1, 'Đã thanh toán'),
    )
    
    customerName = models.CharField('Tên khách hàng', max_length=100)
    phoneNumber    = models.CharField('Số điện thoại', max_length=11)
    email          = models.CharField('Email', null=True, max_length=100, blank=True)
    date = models.DateField('Ngày', null=False)
    time = models.TimeField('Giờ', null=False)
    amount = models.IntegerField('Số lượng',default=0)
    status = models.IntegerField('Trạng thái', choices=STATUS, default=0)
    
    class Meta:
        verbose_name = _("Đặt bàn")
        verbose_name_plural = _("Đặt bàn")
    
    def __str__(self):
      	return self.customerName