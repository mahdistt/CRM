from django.core.validators import RegexValidator
from django.db import models

from product import models as Product

# Check phone number with regular expression
phone_re = RegexValidator(regex='^0[0-9]{2,}[0-9]{7,}$', message='شماره وارد شده صحیح نیست!')


# ('^(\\+98|0)?9\\d{9}$')
# (+98|0|98|0098)?([ ]|-|[()]){0,2}9[0-9]([ ]|-|[()]){0,2}(?:[0-9]([ ]|-|[()]){0,2}){8}/


# Create your models here.
class OrganizationInfo(models.Model):
    """
    Company registration in the CRM
    """
    name = models.CharField(max_length=100, verbose_name="نام سازمان")
    city = models.CharField(max_length=20, verbose_name="محل سازمان")
    number = models.CharField(max_length=11, validators=[phone_re], verbose_name="شماره تلفن سازمان")
    email = models.EmailField(max_length=50, verbose_name="ایمیل سازمان")
    number_of_employees = models.IntegerField(verbose_name="تعداد کارمندان سازمان")
    related_product = models.ManyToManyField('organization.OrganizationProduct', verbose_name='محصولات سازمان')
    introducer_name = models.CharField(max_length=100, verbose_name="نام رابط سازمان ")
    introducer_number = models.CharField(max_length=11, validators=[phone_re], verbose_name="شماره رابط سازمان")
    operator_info = models.ForeignKey('auth.User', on_delete=models.PROTECT, verbose_name='اپراتو')
    created_info = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organization Information'

    def __str__(self):
        return self.name


class OrganizationProduct(models.Model):
    """
     Related manufacture product with our products
    """
    organization_product_name = models.CharField(max_length=100, verbose_name="نام محصولات تولیدی")
    related_product = models.ManyToManyField(Product.ProductInfo, verbose_name='محصولات پیشنهادی ما')

    def __str__(self):
        return self.organization_product_name

    class Meta:
        verbose_name = 'Related'
        verbose_name_plural = 'Related Product'
