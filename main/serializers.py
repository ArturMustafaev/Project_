from main.models import Category, Product
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = 'id product'.split()

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title decriptions price category reviews'.split()
