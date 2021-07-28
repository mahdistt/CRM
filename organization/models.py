from django.core.validators import RegexValidator
from django.db import models

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
    city = models.CharField(max_length=20, verbose_name="نام استان")
    number = models.CharField(max_length=11, validators=[phone_re], verbose_name="شماره تلفن")
    number_of_employees = models.IntegerField(verbose_name="تعداد کارمندان")
    email = models.EmailField(max_length=50, verbose_name="ایمیل")
    introducer_name = models.CharField(max_length=100, verbose_name="نام معرف")
    introducer_number = models.CharField(max_length=11, validators=[phone_re], verbose_name="شماره معرف")
    operator_info = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    created_info = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'organization product'

    def __str__(self):
        return self.name
