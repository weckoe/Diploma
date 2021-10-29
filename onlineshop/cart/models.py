from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product
from django.conf import settings


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)


class CartProduct(models.Model):
    product = models.ForeignKey('catalog.Product', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)


class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, unique=True)


class Order(models.Model):
    user = models.ForeignKey('Customer', on_delete=models.CASCADE)
    products = models.ManyToManyField('CartProduct')
    date = models.DateField(auto_now=True)