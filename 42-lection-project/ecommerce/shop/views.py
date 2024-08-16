from rest_framework import response, status
from rest_framework.decorators import api_view

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer, ProductAddSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(['GET'])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return response.Response(serializer.data)


@api_view(["POST"])
def product_create(request):
    serializer = ProductAddSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = ProductSerializer(product)
    return response.Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def product_update(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return response.Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return response.Response(serializer.data)


@api_view(["POST"])
def category_create(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_201_CREATED)
    return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    serializer = CategorySerializer(category)
    return response.Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
def category_update(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    serializer = CategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return response.Response(serializer.data, status=status.HTTP_200_OK)
    return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def category_delete(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return response.Response(status=status.HTTP_204_NO_CONTENT)
