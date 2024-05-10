from django.shortcuts import render
from django.views.generic import DetailView
from . import models
from .models import Book


def index(request):
    books = models.Book.objects.all()
    categories = models.Category.objects.all()
    context = {
        'books': books,
        'categories': categories,
        'title': 'Список книг',
    }
    return render(request, 'core/index.html', context=context)


def get_category(request, category_id):
    books = models.Book.objects.filter(category=category_id)
    categories = models.Category.objects.all()
    category = models.Category.objects.get(pk=category_id)
    context = {
        'books': books,
        'categories': categories,
        'category': category,
    }
    return render(request, 'core/category.html', context=context)


class BookView(DetailView):
    model = Book
    template_name = 'base.html'
    context_object_name = 'book'
