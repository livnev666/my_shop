from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'slug']
    list_display_links = ['name']
    ordering = ['id']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'slug', 'price', 'available', 'stock', 'image_photo', 'created', 'updated']
    list_display_links = ['id', 'name']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}
    list_filter = ['available', 'created', 'updated']
    ordering = ['id']
    list_per_page = 10

    def image_photo(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60'/>".format(obj.image.url))
    image_photo.__name__ = 'Картинка'
