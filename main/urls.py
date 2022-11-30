from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, 
)
from .views import signup, pedidos

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signup/', signup, name='signup'),
    path('orders/', pedidos, name='signup'),
]