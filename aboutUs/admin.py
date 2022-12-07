from django.contrib import admin
from .models import History, Feedback, RestaurantInfo

# Register your models here.
class RestaurantInfoAdmin(admin.ModelAdmin):
    list_display = ('restaurantName', 'founding', 'image_tag',)

admin.site.register(History)
admin.site.register(Feedback)
admin.site.register(RestaurantInfo, RestaurantInfoAdmin)