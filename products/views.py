from django.shortcuts import get_list_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.serializers import ProductSerializer
from .models import Product

@api_view(['GET'])
def product_list (request):


    return Response ('ok')





