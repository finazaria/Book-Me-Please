from django.db import models
from datetime import date
from mancay.models import Book
from django.contrib.auth.models import User


# BOOK_INTEREST_CHOICES = (
#         ('Fiction', 'FICTION'),
#         ('Non-Fiction', 'NON-FICTION'),
#         ('Historical', 'HISTORICAL'),
#         ('Biography', 'BIOGRAPHY'),
#         ('Self-Development', 'SELF-DEVELOPMENT'),
#         ('Business', 'BUSINESS')
#     )

# # Interest
# class Interest(models.Model):
#     book_interest = models.CharField(
#         max_length=20, 
#         choices=BOOK_INTEREST_CHOICES, default=None)

# # class ProfilePic(models.Model):
# #     title = models.CharField(max_length=100)
# #     profile_pic = models.ImageField(default='default.jpg', upload_to="media")
# #     # class Meta:
# #     #     db_table="gallery"

# # Fav Book (Bisa ditambah pake form)
# class FavoriteBook(models.Model):
#     fav_books = models.ManyToManyField(Book)    # Many to many ke books nya
#     # Restrict => biar book nya gak kedelete juga

# # Books Rec (dialihin ke form lain)
# class BooksRec(models.Model):
#     books_rec = models.ManyToManyField(Book)    # many to many relationship ke book

# Class Profile, karena apparently class User udah ada bawaan dari django
# Jadi ini berfokus pada tampilan profile nya aja
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    member_since = models.DateField(default=date.today())

    profile_pic = models.ImageField(null=True, blank=True)

    # # Si user bisa punya banyak interest, dan satu interest bisa dimiliki oleh banyak user
    # user_interest = models.ManyToManyField(Interest)

    # # satu user hanya memiliki satu data fav book
    # user_fav_book = models.OneToOneField(FavoriteBook, null=True, on_delete=models.CASCADE)

    # # satu user hanya memiliki satu data books rec
    # user_books_rec = models.OneToOneField(BooksRec, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name