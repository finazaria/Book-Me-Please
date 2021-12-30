from django.db import models
from datetime import date
from mancay.models import Book
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    member_since = models.DateField(default=date.today())
    

    profile_pic = models.ImageField(null=True, blank=True)

    INTEREST_CHOICES = (
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Historical', 'Historical'),
        ('Biography', 'Biography'),
        ('Self-Development', 'Self-Development'),
        ('Business', 'Business')
    )

    interest = MultiSelectField(null=True, choices=INTEREST_CHOICES)


    def __str__(self):
        return self.name