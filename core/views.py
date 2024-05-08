from django.shortcuts import render
from . import models


def index(request):
    books = models.Book.objects.all()
    return render(request, 'core/index.html', {'books': books, 'title': 'Список книг'})
