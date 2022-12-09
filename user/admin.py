from django.contrib import admin
from .models import UserProfile, Staff

# Register your models here.
class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'phone', 'email',)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone', 'email', 'BirthDate', 'joinedDate')
    ist_filter = ('status', )

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Staff, StaffAdmin)