from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.OrganizationInfo)
class RegisterOrganization(admin.ModelAdmin):
    list_display = (
        'name',
        'number',
        'number_of_employees',
        'email',
        'introducer_name',
        'introducer_number',
        'operator_info',
        'created_info',
    )
    search_fields = (
        'name',
        'number',
    )

    list_display_links = (
        'name',
    )
    list_editable = (
        'number_of_employees',
    )
    list_filter = (
        'operator_info',
        'number_of_employees',
        'created_info',
    )


@admin.register(models.OrganizationProduct)
class RelatedProduct(admin.ModelAdmin):
    list_display = (
        'pk',
        'organization_product_name',

    )
    search_fields = (
        'organization_product_name',
        'pk',
    )
    list_display_links = (
        'pk',
        'organization_product_name',
    )
