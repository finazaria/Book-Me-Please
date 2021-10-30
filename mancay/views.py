from django.http import response, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from django.db.models import Q



def index(request):
    # return response.HttpResponse("Hello World")
    books = Book.objects.all().order_by('Name')
    response = {'books' : books}
    return render(request, 'index.html', response)


def SearchBar(request):
    # genres = Genre.objects.all().values()

    searched = request.POST['searched']
    books = Book.objects.filter(Q(Name__contains = searched)| Q(Author__contains = searched)).order_by('Name')

    if request.method == "POST":
        return render(request, 'search.html',{'searched':searched, 'books':books} )
    
    else:
        return render(request, 'search.html',{})


def GenreSearch(request):

    # genre1 = request.POST['Action']
    # genre2 = request.POST['Fantasy']

    # if request.POST == genre1:
    #     books = Book.objects.filter(Genre__contains = 'Action')
    #     return render(request, 'searchGenre.html' , {'books':books} )

    # elif request.POST == genre2:
    #     books = Book.objects.filter(Genre__contains = 'Fantasy')
    #     return render(request, 'searchGenre.html' , {'books':books} )


    if request.POST.get('Action'):
        genre = request.POST['Action']
        books = Book.objects.filter(Genre__contains = 'Action').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Comedy'):
        genre = request.POST['Comedy']
        books = Book.objects.filter(Genre__contains = 'Comedy').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Crime'):
        genre = request.POST['Crime']
        books = Book.objects.filter(Genre__contains = 'Crime').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Fantasy'):
        genre = request.POST['Fantasy']
        books = Book.objects.filter(Genre__contains = 'Fantasy').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Historycal'):
        genre = request.POST['Historycal']
        books = Book.objects.filter(Genre__contains = 'Historycal').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Horror'):
        genre = request.POST['Horror']
        books = Book.objects.filter(Genre__contains = 'Horror').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Mystery'):
        genre = request.POST['Mystery']
        books = Book.objects.filter(Genre__contains = 'Mystery').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Myth'):
        genre = request.POST['Myth']
        books = Book.objects.filter(Genre__contains = 'Myth').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Romance'):
        genre = request.POST['Romance']
        books = Book.objects.filter(Genre__contains = 'Romance').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )

    elif request.POST.get('Drama'):
        genre = request.POST['Drama']
        books = Book.objects.filter(Genre__contains = 'Drama').order_by('Name')
        return render(request, 'searchGenre.html' , {'books':books, 'genre':genre} )



        








    # actions = Book.objects.filter(Genre__contains = )
    # if request.method == 'POST':
    #     if request.POST["action"] == "action":
    #         books = Book.objects.filter(Genre__contains = 'Action')
    #         return render(request, 'searchGenre.html',{'books':books})
    # books = Book.objects.all().values()
    # response = {'books' : books}
    # return render(request, 'searchGenre.html', response)

    

    

    
