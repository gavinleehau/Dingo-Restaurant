from django.contrib import admin
from .models import UserProfile, Staff
from django.conf.locale.es import formats as es_formats

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email',)
    add_fieldsets = (
        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
    )
class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone', 'email', 'BirthDate', 'joinedDate', 'image_tag', 'status')
    list_filter = ('status', )

admin.site.register(UserProfile, UserAdmin)
admin.site.register(Staff, StaffAdmin)
