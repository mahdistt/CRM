from django import forms

from organization import models


class OrganizationRegisterForm(forms.ModelForm):
    class Meta:
        model = models.OrganizationInfo
        fields = (
            'name',
            'city',
            'number',
            'email',
            'number_of_employees',
            'related_product',
            'introducer_name',
            'introducer_number',
            'operator_info',

        )

