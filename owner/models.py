from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(
            User,
            on_delete=models.CASCADE,
            primary_key=True
        )
    def save(self, *args, **kwargs):
        if self.user.is_superuser and self.user.is_staff:
            super(Owner, self).save(*args, **kwargs)
        return 
    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.FileField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} -> R${self.price}"
