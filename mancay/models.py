from django.db import models
from django.utils.translation import deactivate

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=100)
    Author = models.CharField(max_length=30)
    Genre = models.CharField(max_length=30)
    Background_photo = models.ImageField(null=True, blank=True)

