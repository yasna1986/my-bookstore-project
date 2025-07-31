from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Category , Book
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
        class Meta:
         model = Book
         fields ='__all__'