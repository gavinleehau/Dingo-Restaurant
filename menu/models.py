from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Food(models.Model):
    image = models.ImageField('Ảnh món ăn')
    foodName = models.CharField('Tên món ăn', max_length=100)
    amount=models.IntegerField('Số lượng',default=0)
    description = models.TextField('Mô tả món ăn')
    price = models.DecimalField('Giá',max_digits=20, decimal_places=0,default=0)
    status = models.BooleanField('Trạng thái món ăn', default=True)

    class Meta:
        verbose_name = _("Thực đơn món")
        verbose_name_plural = _("Thực đơn món")

    # Custom Admin: Function for show image in Blog
    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="90px";/>'.format(self.image.url))
    image_tag.short_description='Image'

    def FormatToVND(self):
        return '{:3,}'.format(self.price) + ' ' + 'đ'
    FormatToVND.short_description = 'Giá'
    
    def __str__(self):
        return self.foodName


