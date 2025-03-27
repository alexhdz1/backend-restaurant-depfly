from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Restaurant
from .serializers import RestaurantSerializer, PatchedRestaurantSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'rating']
    search_fields = ['name']
    ordering_fields = ['rating', 'name']

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return PatchedRestaurantSerializer
        return super().get_serializer_class()

