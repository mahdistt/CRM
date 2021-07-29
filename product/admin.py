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
        'technical_features',
        'taxation',
        'pdf_catalog',
        'img_catalog',


    )
    search_fields = (
        'name',
        'pk',

    )
    list_editable = (
        'price',
    )
    list_filter = (
        'price',
        'taxation',

    )

