from django.shortcuts import render

from rest_framework import viewsets
from products.models import Product, Color
from mytut.serializers import ProductSerializer, ColorSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ColorViewSet(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
