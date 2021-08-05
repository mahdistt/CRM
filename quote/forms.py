from django import forms

from . import models


class QuoteCreateViewForm(forms.ModelForm):
    class Meta:
        model = models.QuoteItem
        fields = (
            'quote',
            'product',
            'price',
            'quantity',
            'discount',
        )
        widgets = {
            'quantity': forms.NumberInput,
            'discount': forms.NumberInput,
            'price': forms.NumberInput,
            'quote': forms.Select,

        }
