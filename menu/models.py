from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Special(models.Model):
    image = models.ImageField('Ảnh món ăn')
    foodName = models.CharField('Tên món ăn', max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    status = models.BooleanField('Trạng thái món ăn', default=True)

    # Custom Admin: Function for show image in Blog
    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="90px";/>'.format(self.image.url))
    image_tag.short_description='Image'

    
    
    def __str__(self):
        return self.foodName

class Breakfast(models.Model):
    image = models.ImageField('Ảnh món ăn')
    foodName = models.CharField('Tên món ăn', max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0,default=0)
    status = models.BooleanField('Trạng thái món ăn', default=True)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="90px";/>'.format(self.image.url))
    image_tag.short_description='Image'
    
    def __str__(self):
        return self.foodName

class Lunch(models.Model):
    image = models.ImageField('Ảnh món ăn')
    foodName = models.CharField('Tên món ăn', max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0,default=0)
    status = models.BooleanField('Trạng thái món ăn', default=True)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="90px";/>'.format(self.image.url))
    image_tag.short_description='Image'
    
    def __str__(self):
        return self.foodName

class Dinner(models.Model):
    image = models.ImageField('Ảnh món ăn')
    foodName = models.CharField('Tên món ăn', max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=0,default=0)
    status = models.BooleanField('Trạng thái món ăn', default=True)

    def image_tag(self):
        return mark_safe('<img src="{}" height="50", width="90px";/>'.format(self.image.url))
    image_tag.short_description='Image'
    
    def __str__(self):
        return self.foodName
