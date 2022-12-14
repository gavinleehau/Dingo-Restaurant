# import Variants as Variants
from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Count
from django.forms import ModelForm

from menu.models import Food


class ShopCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.title

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
        return (self.quantity * self.product.price)

    def countreview(self):
        reviews = ShopCart.objects.filter(product=self, status='True').aggregate(count=Count('id'))
        cnt = 0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt