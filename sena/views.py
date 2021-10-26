from django.http import response, HttpResponseRedirect
from django.shortcuts import render
from mancay.models import *

def index(request):
    books = Book.objects.all().values()
    response = {'books' : books}
    return render(request, 'landing.html', response)

