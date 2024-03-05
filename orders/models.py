from django.db import models
from test_my_shop.models import Product, Category

# Create your models here.


class Order(models.Model):

    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    email = models.EmailField(blank=True, verbose_name='Почта')
    address = models.CharField(max_length=250, blank=True, verbose_name='Адрес')
    postal_code = models.CharField(max_length=20, blank=True, verbose_name='Почтовый индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.first_name}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.order}'

    def get_cost(self):
        return f'{self.price * self.quantity}'

    class Meta:

        verbose_name = 'Элементы заказа'
        verbose_name_plural = 'Элементы заказов'

