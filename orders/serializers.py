from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'items', 'created_at']
        read_only_fields = ['user', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        for item_data in items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            
            # Check stock
            if product.stock < quantity:
                raise serializers.ValidationError(
                    f"Not enough stock for {product.name}!"
                )
            
            # Reduce stock
            product.stock -= quantity
            product.save()
            
            # Create order item
            OrderItem.objects.create(order=order, **item_data)
        
        return order