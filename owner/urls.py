from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ProductAPIView, ProductViewSet

urlpatterns = [
    path('products/', ProductAPIView.as_view(), name='products'),
]
router = SimpleRouter()
router.register('product', ProductViewSet)
urlpatterns += router.urls

