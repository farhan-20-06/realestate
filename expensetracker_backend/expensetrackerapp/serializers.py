from rest_framework import serializers
from .models import Property

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'property_type', 'location', 'land_size_acres', 'asking_price', 'description', 'image', 'created_at', 'updated_at']