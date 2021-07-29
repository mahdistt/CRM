from django.db import models

from organization import models as OrgProduct


# Create your models here.
class ProductInfo(models.Model):
    """
    Product registration in the CRM
    """
    name = models.CharField(max_length=100, verbose_name="نام کالا")
    price = models.PositiveIntegerField(default=0, db_index=True,verbose_name='قیمت')
    taxation = models.BooleanField(verbose_name=" مشمول مالیات؟", default=True)
    img_catalog = models.FileField(verbose_name=' کاتالوگ عکس', upload_to='catalogs/img')
    pdf_catalog = models.ImageField(verbose_name='کاتالوگ پی دی اف', upload_to='catalogs/pdf')
    technical_features = models.TextField(max_length=500, verbose_name='ویژگی های فنی')

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Our Products'

    def __str__(self):
        return self.name
