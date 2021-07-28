from django.contrib import admin

from . import models


# Register your models here.


# Register your models here.
@admin.register(models.ProductInfo)
class RegisterProduct(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'price',
        'pdf_catalog',
        'img_catalog',
        'technical_features',
        'taxation',
    )
    search_fields = (
        'name',
        'description__icontains',
    )
    list_editable = (
        'price',
    )
