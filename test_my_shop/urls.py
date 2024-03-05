from django.urls import path
from test_my_shop import views as views_test_my_shop


urlpatterns = [

    path('', views_test_my_shop.ListProduct.as_view(), name='list-product'),
    path('product/<slug:slug_product>/', views_test_my_shop.DetailProduct.as_view(), name='one_product'),
    path('idproduct/<int:pk>/', views_test_my_shop.DetailProductID.as_view(), name='one_id'),
    path('category/<slug:slug_category>/', views_test_my_shop.CategoryList.as_view(), name='category_list'),

]