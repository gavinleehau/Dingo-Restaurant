from django.contrib import admin
from .models import author, blog, InstagramFeeds
from django.conf.locale.es import formats as es_formats

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    def admin_created_at(self, obj):
        return obj.created_at.strftime('%d-%m-%Y')
    list_display = ('title', 'author', 'created_at', 'image_tag', 'status')
    list_filter = ('status', )
    # search_fields = ['title', 'content']
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(author)
admin.site.register(blog, PostAdmin)
admin.site.register(InstagramFeeds)


