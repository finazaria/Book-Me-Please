from django.http import response, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.db.models import Q



def index(request):
    # return response.HttpResponse("Hello World")
    books = Book.objects.all().values()
    response = {'books' : books}
    return render(request, 'index.html', response)


def SearchBar(request):
    # genres = Genre.objects.all().values()

    searched = request.POST['searched']
    books = Book.objects.filter(Q(Name__contains = searched)| Q(Author__contains = searched))

    if request.method == "POST":
        return render(request, 'search.html',{'searched':searched, 'books':books} )
    
    else:
        return render(request, 'search.html',{})


def GenreSearch(request):
    # actions = Book.objects.filter(Genre__contains = )
    if request.method == 'POST':
        if request.POST["action"] == "action":
            books = Book.objects.filter(Genre__contains = 'Action')
            return render(request, 'searchGenre.html',{'books':books})
    

    

    
