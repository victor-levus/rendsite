from django.contrib import admin

from . import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'category', 'price']
    ordering = ['title']
    list_per_page = 15
