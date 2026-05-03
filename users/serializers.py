from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True, min_length=8)
    confirm_password=serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'phone', 'address']
        
        
    def validate_email(self,value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists!!!")
        return value
        
    def validate(self,data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError("Password doesnot match")
        return data
        
    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user=User.objects.create_user(**validated_data)
        return user