from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Create your models here.

class RestaurantInfo(models.Model):
    restaurantName = models.CharField('Tên nhà hàng', max_length=100)
    logo           = models.ImageField('Logo')
    founding       = models.DateField('Ngày thành lập', null=True)
    # social
    faceBook  = models.CharField("Facebook", default="#", max_length=1000, blank=True)
    twitter   = models.CharField("Twiiter", default="#", max_length=1000, blank=True)
    instagram = models.CharField("Instagram", default="#", max_length=1000, blank=True)
    skype     = models.CharField("Skype", default="#", max_length=1000, blank=True)

    def __str__(self):
        return self.restaurantName
    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="90px";/>'.format(self.logo.url))
    image_tag.short_description='Image'

    class Meta:
        verbose_name = _("Thông tin nhà hàng")
        verbose_name_plural = _("Thông tin nhà hàng")



class History(models.Model):
    title  = models.TextField('Tiêu đề', null=True)
    detail = RichTextUploadingField('Nội dung')
    image  = models.ImageField('Ảnh bài viết', null=True)

    class Meta:
        verbose_name = _("Lịch sử nhà hàng")
        verbose_name_plural = _("Lịch sử nhà hàng")

    def __str__(self):
        return self.title

class Feedback(models.Model):
    customer_avatar = models.ImageField('Ảnh đại diện khách hàng', null=True)
    customer_name = models.CharField('Tên khách hàng', max_length=50)
    feedback      = RichTextUploadingField('Nội dung feedback')
    created_at    = models.DateTimeField('Ngày đăng')

    class Meta:
        verbose_name = _("Phản hồi của khách hàng")
        verbose_name_plural = _("Phản hồi của khách hàng")

    def __str__(self):
        return self.customer_name