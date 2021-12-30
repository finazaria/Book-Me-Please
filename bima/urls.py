from django.urls import path
from bima.views import home,loginView,logoutView,register,interest

urlpatterns = [
    path('', home, name='home'),
    path('loginView',loginView,name="loginView"),
    path('logoutView',logoutView,name="logoutView"),
    path('register',register,name='register'),
    path('interest',interest,name='interest'),
]