from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Review
from .serializers import ReviewSerializer, PatchedReviewSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['restaurant', 'rating', 'name']
    search_fields = ['name', 'description']
    ordering_fields = ['created', 'rating']

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return PatchedReviewSerializer
        return super().get_serializer_class()
