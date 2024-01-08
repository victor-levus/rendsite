from rest_framework import serializers

from superMart.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'title', 'description',
                  'category', 'price', 'image']
