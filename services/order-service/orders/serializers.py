from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product_id', 'product_name', 'quantity', 'price', 'subtotal']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user_id', 'status', 'total_amount', 'shipping_address', 'items', 'created_at', 'updated_at']


class CreateOrderSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    shipping_address = serializers.CharField()
    items = serializers.ListField(child=serializers.DictField())