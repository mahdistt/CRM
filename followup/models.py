from django.db import models

from organization.models import OrganizationInfo


class FollowUp(models.Model):
    """
        The user can follow the organization
    """
    subject = models.CharField(max_length=50, verbose_name='موضوع')
    body = models.TextField(verbose_name='متن پیگیری')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='زمان ثبت پیگیری')
    creator_related = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='اپراتور')
    organization_related = models.ForeignKey(OrganizationInfo, on_delete=models.PROTECT, verbose_name='سازمان')

    def __str__(self):
        return self.subject
