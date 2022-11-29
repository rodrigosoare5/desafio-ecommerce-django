from django.contrib import admin
from .models import  Order
from owner.models import Owner, Product

admin.site.register([Order, Owner, Product])
# Register your models here.
