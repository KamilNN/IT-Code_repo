from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from core import models, filters, serializers


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


class BookModelViewSet(ModelViewSet):
    def get_filters(self):
        return filters.Book(self.request.GET)

    def get_queryset(self):
        return self.get_filters().qs

    queryset = models.Book.objects.all()
    serializer_class = serializers.Book


class Book(APIView):
    def get(self, request):
        qs = models.Book.objects.all()
        prices = [p.price for p in qs]

        return Response(prices)
