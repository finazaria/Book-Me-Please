from django.core.checks import messages
from django.shortcuts import render,redirect
from django.http.response import HttpResponseRedirect
from .models import User, Profile
from .models import *
from mancay.models import Book
from .forms import ProfilePicForm
from django.contrib.auth import authenticate, login, logout
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

def userLogout(request):
    logout(request)
    return redirect('login')

def profilePage(request):
    # profile = request.User.Profile.objects.all()
    # response = {'profile' : profile}      # Iterate user di html nantinya
    return render(request, 'user_profile_details.html')
    # nanti di html tinggal user.profile.attribute

def profilePicForm(request):
    if request.method == "POST":
        # instance nya merupakan info2 yang udah ada dari si user
        form = ProfilePicForm(request.POST, 
        request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()      # Save the form data to model
            messages.success(request, f'Your profile picture has been updated!')
            return redirect('profilePage')
        else:
            messages.error(request, f'There is an error')

    else:
        form = ProfilePicForm(instance=request.user.profile)

    context={'form':form}
    # form untuk ganti prof pic di page terpisah
    return render(request, 'edit_profile_pic.html', context)





# Form interest

# Form FavBook

