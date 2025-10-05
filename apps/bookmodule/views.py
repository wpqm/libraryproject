from django.shortcuts import render,redirect
from django.http import HttpResponse
from django import forms
from django.db.models import Count,Sum,Avg,Max,Q
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')
