from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
