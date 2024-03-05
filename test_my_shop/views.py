from django.shortcuts import render
from .models import Product, Category
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, DetailView, FormView
from cart.forms import CartAddProductForm

# Create your views here.


class ListProduct(ListView):

    model = Product
    template_name = 'test_my_shop/main_page.html'
    context_object_name = 'prod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

            'prod': Product.objects.filter(Q(available=True)),
            'category': Category.objects.all(),
            'title': 'Товары',

        })
        return context
# Product.objects.filter(Q(available=True)),


class CategoryList(ListView):

    template_name = 'test_my_shop/categories.html'
    model = Product
    context_object_name = 'prod'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'prod': Product.objects.all(),
            'cat': Category.objects.get(slug=self.kwargs['slug_category']),
        })
        return context


class DetailProduct(DetailView):

    model = Product
    template_name = 'test_my_shop/detail_product.html'
    context_object_name = 'one_prod'
    slug_url_kwarg = 'slug_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({

            'cart_product_form': CartAddProductForm(),
        })
        return context
#
#     # def get_object(self, queryset=None):
#     #     return get_object_or_404(Product, id=self.kwargs['pk'])
#
#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context.update({
#     #         'one_prod': get_object_or_404(Product, id=self.kwargs['pk'])
#     #     })


class DetailProductID(DetailView):

    model = Product
    template_name = 'test_my_shop/detail_product.html'
    context_object_name = 'one_prod'
    pk_url_kwarg = 'pk'
    slug_url_kwarg = 'slug'
    query_pk_and_slug = True

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update({
    #         'one_prod': get_object_or_404(Product, pk=self.kwargs['pk'])
    #     })
    #     return context




