from django.contrib import admin

from quote import models


@admin.register(models.Quote)
class RelatedProduct(admin.ModelAdmin):
    list_display = (
        'creator',
        'organization_related',
        'created_info',
    )
    search_fields = (
        'created_info',
    )

    list_filter = (
        'organization_related',
        'creator',
        'created_info',

    )


@admin.register(models.QuoteItem)
class RelatedProduct(admin.ModelAdmin):
    list_display = (
        'quote',
        'product',
        'price',
        'quantity',
        'discount',
    )
    search_fields = (
        'quantity',

    )

    list_filter = (
        'quote',
        'product',
        'price',
        'quantity',
        'discount',
    )
    list_editable = (
        'quantity',
        'discount',
    )
