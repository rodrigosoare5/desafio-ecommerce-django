from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Order

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "password")

        extra_kwargs = {
            "password": {"write_only": True},
        }
        def create(self,validated_data):
            user = User.objects.create(validated_data['username'],validated_data['email'],validated_data['password'])
            return user


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"



