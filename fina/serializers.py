from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'name', 'member_since', 
        'profile_pic', 'interest']