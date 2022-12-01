from rest_framework.parsers import  MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from .serializers import ProductSerializer
from .models import Product, Owner
from rest_framework import filters, generics

class ProductAPIView(generics.ListAPIView):
    search_fields = ['name']
    filter_backends = (filters.SearchFilter,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class IsSuperUser(IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser and request.user.owner)

class ProductViewSet(ModelViewSet):
    parser_classes = ( MultiPartParser, FormParser)
    permission_classes = (IsSuperUser, IsAuthenticated)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['post' ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user.owner)




