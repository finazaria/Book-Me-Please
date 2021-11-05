from django.http import response, HttpResponseRedirect
from django.shortcuts import render
from mancay.models import *
from .forms import CommentForm

def index(request):
    books = Book.objects.all().values()
    response = {'books' : books}
    return render(request, 'landing.html', response)
