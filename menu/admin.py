from django.contrib import admin
from .models import Special, Breakfast, Lunch, Dinner

# Register your models here.


class SpecialAdmin(admin.ModelAdmin):
    list_display = ('foodName', 'price', 'status', 'image_tag')
    list_filter = ('status',)

    def price(self, obj: Special) -> str:
        return f"{(obj.price * Decimal(0.5)):.2f}$"

class BreakfastAdmin(admin.ModelAdmin):
    list_display = ('foodName', 'price', 'status', 'image_tag')
    list_filter = ('status',)

class LunchAdmin(admin.ModelAdmin):
    list_display = ('foodName', 'price', 'status', 'image_tag')
    list_filter = ('status',)

class DinnerAdmin(admin.ModelAdmin):
    list_display = ('foodName', 'price', 'status', 'image_tag')
    list_filter = ('status',)

admin.site.register(Special, SpecialAdmin)
admin.site.register(Breakfast, BreakfastAdmin)
admin.site.register(Lunch, LunchAdmin)
admin.site.register(Dinner, DinnerAdmin)
