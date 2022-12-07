from django.contrib import admin
from .models import author, blog, InstagramFeeds

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_at', 'image_tag')
    list_filter = ('status',)
    # search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(author)
admin.site.register(blog, PostAdmin)
admin.site.register(InstagramFeeds)
