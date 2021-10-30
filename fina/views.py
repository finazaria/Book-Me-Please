from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http.response import HttpResponseRedirect
from .models import User, Profile
from .models import *
from mancay.models import Book
from .forms import ProfilePicForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def userLogin(request):
    if request.method == "POST":
        # username = request.POST.get('username')     # '' => the name of the tag tadi di html
        # password = request.POST.get('password')
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # return render(request, 'user_profile_details.html')
            return redirect('profilePage')
        
        else:
            messages.info(request, "Wrong username/password")
            return redirect('login')
        
    context={}
    return render(request, 'login.html', context)
    

def profilePage(request):
    profile = Profile.objects.all()
    response = {'profile' : profile}      # Iterate user di html nantinya
    return render(request, 'user_profile_details.html', response)

def profilePicForm(request):
    user = request.user
    context={}
    form = ProfilePicForm(instance=user)
    
    if form.is_valid() and request.method == "POST":
        # Save the form data to model
        form.save()
        # return HttpResponseRedirect("/lab-4")      # To redirect to /lab-4 after validating and saving the data

    context['form'] = form
    # form untuk ganti prof pic di page terpisah
    return render(request, 'edit_profile_pic.html', context)





# Form interest

# Form FavBook

