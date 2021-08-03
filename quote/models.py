from django.contrib.auth import get_user_model
from django.db import models

from organization.models import OrganizationInfo
from product.models import ProductInfo


class Quote(models.Model):
    """
    Create a quote by user
    """
    creator = models.ForeignKey(get_user_model(), on_delete=models.PROTECT, verbose_name='نام ادمین')
    organization_related = models.ForeignKey(OrganizationInfo, on_delete=models.PROTECT, verbose_name='شرکت')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return self.organization_related


class QuoteItem(models.Model):
    """
    Quote items are generated here
    """
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name='اقلام پیش فاکتور')
    product = models.ForeignKey(ProductInfo, on_delete=models.PROTECT, verbose_name='محصولات شرکت')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    discount = models.PositiveIntegerField(default=0, verbose_name='تخفیف')

    def __str__(self):
        return self.quote
