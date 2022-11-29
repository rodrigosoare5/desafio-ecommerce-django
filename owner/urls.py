from django.urls import path

from .views import products, product

urlpatterns = [
    path('product/', product, name='product'),
    path('products/', products, name='products'),
]