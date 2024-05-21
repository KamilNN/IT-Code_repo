from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, RedirectView, FormView
from core import models, forms


def index(request):
    books = models.Book.objects.all()
    categories = models.Category.objects.all()
    context = {
        'books': books,
        'categories': categories,
        'title': 'Список книг',
    }
    return render(request, 'core/index.html', context=context)


class ClassBasedIndex(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = models.Book.objects.all()
        categories = models.Category.objects.all()
        context['books'] = books
        context['categories'] = categories
        context['title'] = 'Список книг'
        return context


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


class BookList(ListView):
    model = models.Book
    context_object_name = 'books'
    template_name = 'core/book_list.html'


class BookView(DetailView):
    model = models.Book
    template_name = 'core/book_view.html'
    context_object_name = 'book'


class Redirect(RedirectView):
    query_string = True
    url = 'https://en.wikipedia.org/wiki/Ray_Bradbury'


class SimpleForm(FormView):
    template_name = 'core/forms.html'
    form_class = forms.SimpleForm
    success_url = "/index_class/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
