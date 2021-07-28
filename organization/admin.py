from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.OrganizationInfo)
class RegisterOrganization(admin.ModelAdmin):
    list_display = (
        'pk',
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
        'description__icontains',
    )
