from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True, null=True, blank=True, verbose_name='URL')

    def __str__(self):
        return f'{self.name}'

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super(Category, self).save(*args, **kwargs)

    def get_url_cat(self):
        return reverse('category_list', kwargs={'slug_category': self.slug})

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):

    name = models.CharField(max_length=200, db_index=True, verbose_name='Наименование товара')
    slug = models.SlugField(max_length=200, db_index=True, null=True, blank=True, verbose_name='URL')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True, verbose_name='Наличие товара')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, verbose_name='Номер категории', related_name='products')

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('one_product', args=[self.slug])

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'




