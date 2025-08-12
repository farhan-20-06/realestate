from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property-list'),
    path('properties/<int:pk>/', views.property_detail, name='property-detail'),
]
