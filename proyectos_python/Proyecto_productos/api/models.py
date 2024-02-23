
# models.py
from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Productos(models.Model):
    nomProducto = models.CharField(max_length=50)
    desProducto = models.CharField(max_length=200)
    catProducto = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    canProducto = models.PositiveIntegerField(default=True)
    preProducto = models.PositiveBigIntegerField(default=True)
    estProducto = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} - {self.nomProducto}'


class Operator(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento_identidad = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Customer(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    documento_identidad = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ManyToManyField(Productos)
    quantity = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()
