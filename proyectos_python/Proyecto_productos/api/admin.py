from django.contrib import admin
from .models import Productos, Order, OrderItem, Categoria, Operator, Customer

# Register your models here.
admin.site.register(Productos)
admin.site.register(Order)
admin.site.register(Categoria)
admin.site.register(OrderItem)
admin.site.register(Customer)
admin.site.register(Operator)
