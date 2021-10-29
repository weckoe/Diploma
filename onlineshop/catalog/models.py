from django.db import models
from .validators import image_resolution_check_small, image_resolution_check_big, image_resolution_check_cart


# Create your models here.
class Addon(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')

    class Meta:
        verbose_name = 'Акссесуар'
        verbose_name_plural = 'Акссесуары'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=300, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,
                                 verbose_name='Категория')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')
    addons = models.ManyToManyField(Addon)
    image = models.ImageField(validators=[image_resolution_check_small], upload_to="static/img",
                              verbose_name="Маленькое Изображение", null=True, blank=True)
    big_image = models.ImageField(validators=[image_resolution_check_big], upload_to="static/img",
                                  verbose_name="Большое Изображение", null=True, blank=True)
    cart_image = models.ImageField(validators=[image_resolution_check_cart], upload_to="static/img",
                                   verbose_name="Изображение для таблицы", null=True, blank=True)
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество на складе')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30, verbose_name='Наименование')
    description = models.TextField(max_length=500, verbose_name='Описание')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='url')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
