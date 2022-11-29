from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserCreateSerializer, OrderSerializer
from .models import Order

@api_view(["POST"])
def signup(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def pedidos(request, format=None):
    if request.method == "GET":
        try:
            user = request.user
            pedidos = Order.objects.filter(customer=user).order_by('-id') 
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer = OrderSerializer(
            pedidos, context={'request': request}, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        pedido = request.data
        serializer = OrderSerializer(data=pedido)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

