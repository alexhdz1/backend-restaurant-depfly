from rest_framework import serializers
from .models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()
    image = serializers.ImageField(required=True)

    class Meta:
        model = Restaurant
        fields = ['slug', 'name', 'url', 'image', 'rating']

class PatchedRestaurantSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Restaurant
        fields = ['slug', 'name', 'url', 'image', 'rating']        
        extra_kwargs = {
            'name': {'required': True},
            'url': {'required': False, 'allow_null': True},
            'image': {'required': True},
        }
