from django.db import models

from organization import models as OrgProduct


# Create your models here.
class ProductInfo(models.Model):
    """
    Product registration in the CRM
    """
    name = models.CharField(max_length=100, verbose_name="نام کالا")
    price = models.PositiveIntegerField(default=0, db_index=True)
    pdf_catalog = models.ImageField(verbose_name='عکس کاتالوگ', upload_to='catalogs/pdf')
    img_catalog = models.FileField(verbose_name='پی دی اف کاتالوگ', upload_to='catalogs/img')
    technical_features = models.TextField(max_length=500, verbose_name='ویژگی های فنی')
    taxation = models.BooleanField(verbose_name="آیا مشمول مالیات می باشد ؟", default=True)
    related_product = models.ManyToManyField(OrgProduct.OrganizationInfo, verbose_name='محصولات مرتبط')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name
