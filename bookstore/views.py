from django.shortcuts import render
from .models import Book
# Create your views here.
def all_book(requset):
    all_book=Book.objects.all()
    return render(requset,'bookstore/all_book.html',locals())