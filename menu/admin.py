from django.contrib import admin
from .models import Food

# Register your models here.


class FoodAdmin(admin.ModelAdmin):
    list_display = ('foodName', 'FormatToVND', 'status', 'image_tag')
    list_filter = ('status',)

admin.site.register(Food, FoodAdmin)
