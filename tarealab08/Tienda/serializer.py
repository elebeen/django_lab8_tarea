from rest_framework import serializers # type: ignore
from .models import Product, Suplier, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'category': {'required': True},
            'suplier': {'required': True}
        }

class SuplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suplier
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'contact_info': {'required': True}
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'name': {'required': True},
            'description': {'required': True}
        }