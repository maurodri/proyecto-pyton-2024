from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductosSerializer, OrderSerializer, OrderItemSerializer, CategoriaSerializer, OperatorSerializer, CustomerSerializer
from .models import Productos, Order, OrderItem, Categoria, Operator, Customer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()

        # Calcula el precio total y subtotal
        total_price = 0
        subtotal = 0
        for product_id in data.getlist('product'):
            product = Productos.objects.get(id=product_id)
            total_price += float(product.preProducto) * \
                float(data['quantity']) - float(data['discount'])
            subtotal += float(product.preProducto) * float(data['quantity'])

        # Agrega el precio total y subtotal al data del request
        data['total_price'] = total_price
        data['subtotal'] = subtotal

        # Actualiza request.data con la nueva data
        request._full_data = data

        # Llama al método create original
        return super().create(request, *args, **kwargs)


class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
