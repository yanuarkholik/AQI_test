from django.http import HttpResponse
from requests import request
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect

from .models import Book

def book(request):
    """ Output book """
    book = Book.objects.all()
    context = {
        'book': book
    }
    return render(request, 'templates/home.html', context)