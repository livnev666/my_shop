from django.apps import AppConfig


class TestMyShopConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test_my_shop'
    verbose_name = 'Мой магазин'
