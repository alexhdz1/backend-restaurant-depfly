from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = '__all__'

class PatchedReviewSerializer(serializers.ModelSerializer):
    slug = serializers.ReadOnlyField()
    created = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = ['slug', 'restaurant', 'name', 'description', 'rating', 'created']
        extra_kwargs = {
            'restaurant': {'required': False},
            'name': {'required': False},
            'description': {'required': False},
            'rating': {'required': False},
        }
