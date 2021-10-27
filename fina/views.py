from django.shortcuts import render
from .models import User
from mancay.models import Book

def index(request):
    user = User.objects.all().values()
    response = {'user' : user}
    return render(request, 'user_profile_details.html', response)

# Form profile picture

# Form interest

# Form FavBook

