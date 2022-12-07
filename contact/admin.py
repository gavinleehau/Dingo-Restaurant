from django.contrib import admin
from .models import ContactInfo, Reservations

# Register your models here.

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phoneNumber', 'email',)

admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Reservations)