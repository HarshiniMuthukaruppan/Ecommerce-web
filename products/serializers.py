from rest_framework import serializers
from .models import Product,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'

    def validate_name(self,data):
        if len(data)<3:
            raise serializers.ValidationError("Length of the name should be greater than 3")

        return data     

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        #fields='__all__'
        exclude=['created_at']

    def validate_price(self,value):
        
        if value<=0:
            raise serializers.ValidationError("Price must be greater than 0.")

        return value

    def validate_stock(self,value):

        if value<0:
            raise serializers.ValidationError("Stock can not be negative!")   

        return value

    def validate_name(sel,value):

        if len(value)<3:
            raise serializers.ValidationError("Length of the name should be greater than 3.")      

        return value          
    
    def validate(self, data):

        if data['stock'] == 0 and data['price'] > 100000:

            raise serializers.ValidationError(
                "A product with zero stock cannot have a price above 100,000!"
            )
        return data
