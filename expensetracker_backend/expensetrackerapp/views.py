from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Q
from .models import Property
from .serializers import PropertySerializer

@api_view(['GET', 'POST'])
def property_list(request):
    if request.method == 'GET':
        # Get query parameters for filtering
        property_type = request.GET.get('property_type')
        location = request.GET.get('location')
        land_size_acres = request.GET.get('land_size_acres')
        max_price = request.GET.get('max_price')
        
        # Start with all properties
        properties = Property.objects.all()
        
        # Apply filters if provided
        if property_type:
            properties = properties.filter(property_type__iexact=property_type)
        
        if location:
            properties = properties.filter(location__icontains=location)
        
        if land_size_acres:
            try:
                land_size = float(land_size_acres)
                properties = properties.filter(land_size_acres=land_size)
            except ValueError:
                pass
        
        if max_price:
            try:
                max_price_value = float(max_price)
                properties = properties.filter(asking_price__lte=max_price_value)
            except ValueError:
                pass
        
        serializer = PropertySerializer(properties, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def property_detail(request, pk):
    try:
        property = Property.objects.get(pk=pk)
    except Property.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        property.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
