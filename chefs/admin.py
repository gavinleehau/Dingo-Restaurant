from django.contrib import admin
from .models import Chefs

# Register your models here.

class ChefsAdmin(admin.ModelAdmin):
    list_display = ('fullName', 'position', 'yearOfBirth', 'joiningDate',)
    list_filter = ('position',)

admin.site.register(Chefs, ChefsAdmin)
