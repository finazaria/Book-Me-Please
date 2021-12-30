from django.db import models
from mancay.models import Book

class Comment(models.Model):
    book = models.ForeignKey(Book, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    
        return '%s' % (self.book.pk)
    def get_book(self):
        return self.book.pk


# Create your models here.
