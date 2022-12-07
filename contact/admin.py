from django.contrib import admin
from .models import ContactInfo, Reservations

# Register your models here.

class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'phoneNumber', 'email',)

class ReservationsAdmin(admin.ModelAdmin):
    list_display = ('customerName', 'phoneNumber', 'email', 'date', 'amount', 'status')
    list_filter = ('status',)

admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(Reservations, ReservationsAdmin)