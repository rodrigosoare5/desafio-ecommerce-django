from django.urls import path

from .views import ProductAPIView, product

urlpatterns = [
    path('product/', product, name='product'),
    path('products/', ProductAPIView.as_view(), name='products'),
]