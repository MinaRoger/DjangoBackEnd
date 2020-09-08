from django.shortcuts import render

from rest_framework import viewsets
from products.models import Product
from mytut.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
