from django.db import models
from django.db.models import CASCADE
from django.contrib.auth.models import User
from owner.models import Product


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=CASCADE)
    date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = (
        ("E", "Em espera"),
        ("A", "Aceito"),
        ("R", "Rejeitado"),
    )
    status = models.CharField(max_length=1, choices=STATUS, default="E")
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"Pedido nº {self.id} do cliente {self.customer.user.username}"



