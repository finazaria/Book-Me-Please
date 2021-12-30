from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from bima.models import *
from bima.regist import CreateUserForm

def home(request):
    context = {'page_title':'Home'}
    
    template = None;
    if request.user.is_authenticated:
        template = "indexx.html"
    else:
        template = "anonym_home.html"
    # print(request.user.is_authenticated)

    return render(request,template,context)

def interest(request):
    context = {'page_title':'interest'}

    
    return render(request,'interest.html',context);

def register(request):
    form = CreateUserForm()
    context = {'form':form}
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Akun berhasil dibuat")
            return redirect('loginView')

    return render(request, 'register.html',context)


def loginView(request):
    context = {'page_title':'LOGIN',}

    if request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['password']
        user = authenticate(request, username=username,password=pw)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Silahkan cek kembali")
            return redirect('loginView')
    
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request,'loginView.html',context)
    
            

@login_required
def logoutView(request):
    context = {'page_title':'logout'}
    if request.method == "POST":
        if request.POST["logout"] == "Submit":
            logout(request)
        return redirect('home')
    return render(request,'logoutView.html',context)