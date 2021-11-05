from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', userLogin, name='login'),
    path('logout', userLogout, name='logout'),
    path('profile', profilePage, name='profilePage'),   # fina/profile
    path('profile/edit-profile-picture', profilePicForm, name='profilePicForm'),
    path('profile/add-interest', addInterestForm, name='addInterestForm')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)