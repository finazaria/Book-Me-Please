from django.http import response, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import Comment
from .serializers import commentSerializer
from mancay.models import *
from .forms import CommentForm

import traceback

def index(request):
    books = Book.objects.all().values()
    response = {'books' : books}
    return render(request, 'landing.html', response)

class comment_list(APIView):
    def get_queryset(self):
        commentAll = Comment.objects.all()
        return commentAll

    def get(self, request, *args, **kwargs):
        try:
            buku = request.query_params["book"]
            if buku != None :
                comment = Comment.objects.filter(book=buku)
                serializer = commentSerializer(comment, many=True)
        except Exception:
            print(traceback.format_exc())
            comment = Comment.objects.all()
            serializer = commentSerializer(comment, many=True)

        return Response(serializer.data)

    def post(self):
        pass
