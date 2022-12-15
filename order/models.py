
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from menu.models import Food


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField(null=True)

    def FormatToVND(self):
        return '{:3,}'.format(self.price) + ' ' + 'đ'
    FormatToVND.short_description = 'Giá'

    def __str__(self):
        return self.product.foodName

    class Meta:
        verbose_name = _("Giỏ hàng")
        verbose_name_plural = _("Giỏ hàng")

    @property
    def price(self):
        if self.product_id is not None:
            return (self.product.price)

    @property
    def amount(self):
        if self.product_id is None:
            return None
        return (self.quantity * self.product.price)

    @property
    def varamount(self):
        return (self.quantity * self.product.price) #Tổng tiền của món đó = số lượng món đó * giá tiền món đó

    def countreview(self):
        reviews = ShopCart.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt


class Order(models.Model):
    STATUS = (
        (0, 'Mới'),
        (1, 'Đã thanh toán'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField('Họ và tên', max_length=20, default='')
    email = models.CharField('Email', max_length=50, default='', blank=True)
    phone = models.CharField('Số điện thoại',max_length=20)
    address = models.CharField('Địa chỉ',max_length=150)
    total = models.DecimalField('Tổng cộng',max_digits=100, decimal_places=0,default=0)
    status = models.IntegerField('Trạng thái',choices=STATUS, default=0)
    ip = models.CharField('Địa chỉ ip khách hàng', blank=True, max_length=20)
    adminnote = models.CharField('Ghi chú quản trị viên',blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    @property
    def amount(self):
        if self.product_id is None:
            return None
        return (self.quantity * self.product.price)

    def FormatToVND(self):
        return '{:3,}'.format(self.total) + ' ' + 'đ'
    FormatToVND.short_description = 'Giá'

    class Meta:
        verbose_name = _("Đơn hàng")
        verbose_name_plural = _("Đơn hàng")

    def __str__(self):
        return self.full_name


class OrderProduct(models.Model):
    STATUS = (
        ('Mới', 'Mới'),
        ('Chấp Nhận', 'Chấp Nhận'),
        ('Đã hủy', 'Đã hủy'),
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name=('Món ăn'))
    image = models.ImageField(default=0)
    quantity = models.IntegerField('Số lượng')
    price = models.DecimalField('Giá',max_digits=100, decimal_places=0,default=0)
    amount = models.FloatField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='New', verbose_name=('Trạng thái'))
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


    def amount(self):
        if self.product_id is None:
            return None
        return '{:3,}'.format((self.quantity * self.product.price)) + ' ' + 'đ'
    amount.short_description = 'Tổng giá tiền một món'

    def FormatToVND(self):
        return '{:3,}'.format(self.price) + ' ' + 'đ'
    FormatToVND.short_description = 'Đơn giá'

    class Meta:
        verbose_name = _("Món ăn đã được đặt")
        verbose_name_plural = _("Món ăn đã được đặt")

    def __str__(self):
        return self.product.foodName


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'address', 'phone']


class ShopCartForm(ModelForm):
    class Meta:
        model = ShopCart
        fields = ['quantity']