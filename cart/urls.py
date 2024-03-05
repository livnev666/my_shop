from django.urls import path
from cart import views as cart_views

app_name = 'cart'

urlpatterns = [
    path('cart_detail', cart_views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', cart_views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', cart_views.cart_remove, name='cart_remove'),

]
