from django.db.models import fields
from rest_framework import serializers
from .models import Book

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','Name', 'Author', 'Genre', 'Background_photo']
