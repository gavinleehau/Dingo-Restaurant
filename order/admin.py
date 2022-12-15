from django.contrib import admin
from order.models import ShopCart, Order, OrderProduct

# Register your models here.


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product','user', 'quantity', 'FormatToVND',]
    list_filter = ['user']

    def percentage(sef, obj):
        return round(
           obj.todo_set.filter(state=True).count() * 100 / obj.todo_set.all().count()
        )

class OrderProductline(admin.TabularInline):
    model = OrderProduct
    fields = ('user', 'product','quantity','FormatToVND','amount')
    readonly_fields = ('user', 'product','quantity','FormatToVND','amount')
    can_delete = False
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'FormatToVND', 'status']
    list_filter = ['status']
    # readonly_fields = ('full_name','address','phone','ip','phone','total')
    can_delete = False
    inlines = [OrderProductline]

class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product','quantity', 'FormatToVND',]
    list_filter = ['user']

admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
