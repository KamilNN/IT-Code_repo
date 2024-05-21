from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('index_class/', ClassBasedIndex.as_view(), name='index_class'),
    path('book_list/', BookList.as_view(), name='book_list'),
    path('book/<int:pk>/', BookView.as_view(), name='book_view'),
    path('redirect/', Redirect.as_view(), name='redirect'),
    path('forms/', SimpleForm.as_view(), name='forms'),
    path('category/<int:category_id>', get_category, name='category'),
]
