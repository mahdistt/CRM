from django import forms

from . import models


class FollowUpCreateForm(forms.ModelForm):
    """
        follow up form with register creator info and data time automatically
    """

    def __init__(self, *args, **kwargs):
        self.creator_info = kwargs.pop('creator_info')
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.FollowUp
        fields = [
            'subject',
            'body',
            'organization_related',
        ]
        widgets = {
            'organization_related': forms.Select,
            'body': forms.Textarea
        }
