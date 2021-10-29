from django.contrib import admin
from . import models


# Register your models here.

@admin.register(models.Addon)
class AddonAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
