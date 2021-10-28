from django.urls import path, include
from django.contrib import admin
from .views import *


urlpatterns = [
    path('admin', admin.site.urls),
    path('', index, name='index'),
    path('searchbox', SearchBar, name='SearchBar'),
    path('searchGenre', GenreSearch, name='GenreSearch'),
#     path('searchGenre', searchGenre2, name='GenreSearch'),
]