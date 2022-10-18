import datetime as datetime
from django.contrib.auth.models import User
from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')

    def __str__(self):
        return self.name


class Good(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(max_length=256, verbose_name='описание')

    def __str__(self):
        return self.name


class Item(models.Model):
    code = models.ForeignKey(Good, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    count = models.IntegerField(default=0)
    company = models.ForeignKey(Shop, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'items'
        verbose_name = 'item'

    def __str__(self):
        return f'{str(self.id)} code {self.code} price {self.price} count {self.count} company {self.company}'


class ShoppingCart(models.Model):
    items = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description = models.CharField(max_length=100, verbose_name='чек')
    check_sum = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='цена')
    datetime = models.DateField(auto_now=True)