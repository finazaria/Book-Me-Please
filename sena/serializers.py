from django.db.models import fields
from rest_framework import serializers
from .models import Comment

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['book', 'name', 'comment', 'created_on']