# serializers.py
from rest_framework import serializers
from .models import Productos, Order, OrderItem, Categoria, Operator, Customer


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class ProductosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    operator_name = serializers.ReadOnlyField(source='operator.nombre')
    operator_apellido = serializers.ReadOnlyField(source='operator.apellido')
    operator_documento_identidad = serializers.ReadOnlyField(
        source='operator.documento_identidad')
    customer_name = serializers.ReadOnlyField(source='customer.nombre')
    customer_apellido = serializers.ReadOnlyField(source='customer.apellido')
    customer_documento_identidad = serializers.ReadOnlyField(
        source='customer.documento_identidad')

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'operator', 'customer', 'operator_name', 'operator_apellido',
                  'operator_documento_identidad', 'customer_name', 'customer_apellido', 'customer_documento_identidad']


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.StringRelatedField(
        source='product.nomProducto', many=True)
    product_id = serializers.StringRelatedField(source='product.id', many=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'price',
                  'discount', 'product_name', 'product_id', 'total_price']


class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Productos.objects.all())
    total_price = serializers.SerializerMethodField()
    subtotal = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity',
                  'discount', 'total_price', 'subtotal']

    def get_total_price(self, obj):
        total_price = 0
        for product in obj.product.all():
            total_price += product.preProducto * obj.quantity - obj.discount
        return total_price

    def get_subtotal(self, obj):
        subtotal = 0
        for product in obj.product.all():
            subtotal += product.preProducto * obj.quantity
        return subtotal
