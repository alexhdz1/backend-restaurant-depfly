# review/urls.py
from django.urls import path
from .views import ReviewViewSet
from restaurant.views import RestaurantViewSet

review_list = ReviewViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

review_detail = ReviewViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

restaurant_list = RestaurantViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

restaurant_detail = RestaurantViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    # Restaurant endpoints
    path('reviews/restaurant/', restaurant_list, name='restaurant-list'),
    path('reviews/restaurant/<slug:slug>/', restaurant_detail, name='restaurant-detail'),
    path('reviews/review/', review_list, name='review-list'),
    path('reviews/review/<slug:slug>/', review_detail, name='review-detail'),
]
