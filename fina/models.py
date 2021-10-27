from django.db import models
from datetime import date
from mancay.models import Book

# Interest
class Interest(models.Model):
        # satu variable aja => interest
        
        # First element : the actual value yang di set di model
        # Second element : human readable names nya

    book_interest_choices = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Historical', 'Historical'),
        ('Biography', 'Biography'),
        ('Self-Development', 'Self-Development'),
        ('Business', 'Business')
    ]
    
    book_interest = models.CharField(
        max_length=100,
        choices=book_interest_choices,
    )

# Fav Book (Bisa ditambah pake form)
class FavoriteBook(models.Model):
    fav_books = models.ManyToManyField(Book)    # Many to many ke books nya

# Books Rec (dialihin ke form lain)
class BooksRec(models.Model):
    books_rec = models.ManyToManyField(Book)    # many to many relationship ke book

# User
class User(models.Model):
    name = models.CharField(max_length=40, primary_key=True)  # display name bisa diedit
    member_since = models.DateField(default=date.today())

    # Si user bisa punya banyak interest, dan satu interest bisa dimiliki oleh banyak user
    user_interest = models.ManyToManyField(Interest)

    profile_pic = models.ImageField()

    # satu user hanya memiliki satu data fav book
    user_fav_book = models.OneToOneField(FavoriteBook, on_delete=models.CASCADE)

    # satu user hanya memiliki satu data books rec
    user_books_rec = models.OneToOneField(BooksRec, on_delete=models.CASCADE)