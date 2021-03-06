from django.db import models
from django.db.models import Sum, F

from organization.models import OrganizationInfo
from product.models import ProductInfo


class Quote(models.Model):
    """
    Create a quote by user
    """
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='نام ادمین')
    organization_related = models.ForeignKey(OrganizationInfo, on_delete=models.PROTECT, verbose_name='شرکت')
    created_info = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    def __str__(self):
        return f'{self.organization_related}'

    def get_quantity(self):
        return self.quoteitem_set.all().aggregate(Sum('quantity')).get('quantity__sum', 0)

    def get_total_quote_price(self):
        """
        Total price without taxation and discount
        """
        return self.quoteitem_set.all().annotate(
            total_quote_price=F('price') * F('quantity')).aggregate(
            Sum('total_quote_price'))['total_quote_price__sum']

    def get_quote_discount(self):
        """
        Return total quote discount
        """
        return self.quoteitem_set.all().annotate(
            total_quote_price=F('price') * F('quantity')).annotate(
            calculate_discount=(F('total_quote_price') * F('discount') / 100)).aggregate(
            Sum('calculate_discount'))['calculate_discount__sum']

    def get_quote_taxation(self):
        """
        Calculate 9% taxation if boolean is TRUE
        """
        if ProductInfo.taxation:
            total, discount = self.get_total_quote_price(), self.get_quote_discount()
            return (total - discount) * 0.09
        else:
            return 0

    def get_final_quote_price(self):
        """
        Return final quote price
        """
        total, discount, taxation = self.get_total_quote_price(), self.get_quote_discount(), self.get_quote_taxation()
        return (total - discount) + taxation


class QuoteItem(models.Model):
    """
    Quote items are generated here
    """
    quote = models.ForeignKey(Quote, on_delete=models.CASCADE, verbose_name='پیش فاکتور')
    product = models.ForeignKey(ProductInfo, on_delete=models.PROTECT, verbose_name='محصولات شرکت')
    price = models.PositiveIntegerField(default=0, verbose_name='قیمت')
    quantity = models.PositiveIntegerField(default=1, verbose_name='تعداد')
    discount = models.PositiveIntegerField(default=0, verbose_name='تخفیف')

    def __str__(self):
        return f'{self.quote}'

    def get_total_price(self):
        return self.price * self.quantity


class EmailHistory(models.Model):
    """
     Save email status
    """
    creator = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='نام ادمین')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    email = models.CharField(max_length=100, verbose_name='ایمیل')

    def __str__(self):
        return f'{self.creator}'
