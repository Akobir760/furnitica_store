from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True, verbose_name=_('created_at'))
    updated_at = models.DateField(auto_now=True, verbose_name=_('updated_at'))

    class Meta:
        abstract = True


class CategoryModel(BaseModel):
    name = models.CharField(max_length=100, verbose_name=_('name'))
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')



class CatalogModel(BaseModel):
    title = models.CharField(max_length=50, verbose_name=_('title'))

    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = _('Catalog')
        verbose_name_plural = _('Catalogs')


class ProductModel(BaseModel):
    name = models.CharField(max_length=120, verbose_name=_('name'))
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, verbose_name=_('category'))
    catalog = models.ForeignKey(CatalogModel, on_delete=models.CASCADE, verbose_name=_('catalog'))
    price = models.SmallIntegerField(verbose_name=_('price'))
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name=_('image'))
    short_description = models.TextField(verbose_name=_('short_description'))
    long_description = models.TextField(verbose_name=_('long_description'))


    def __str__(self):
        return f"{self.name} | {self.short_description}"
    

    class Meta:
        verbose_name = _("product")
        verbose_name_plural = _("products")


