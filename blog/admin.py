from django.contrib import admin
from django.conf.locale.es import formats as es_formats
from mptt.admin import DraggableMPTTAdmin

from .models import Category, author, blog, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','status']
    list_filter = ['status']



class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                blog,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 blog,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'image_tag', 'status')
    list_filter = ('status', )
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'comment', 'created_at')

admin.site.register(Category,CategoryAdmin2)
admin.site.register(author)
admin.site.register(blog, PostAdmin)
admin.site.register(Comment, CommentAdmin)


