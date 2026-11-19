from django.shortcuts import render
from .models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'page_title': 'Minu raamatukogu',
        'books': books,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')

def available(request):
    available_books = Book.objects.filter(is_available=True)
    context = {
        'page_title': 'Saadaval olevad raamatud',
        'available_books': available_books,
    }
    return render(request, 'available.html', context)