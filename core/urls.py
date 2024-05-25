from rest_framework.routers import DefaultRouter
from core import views
from django.urls import path
from .views import *

router = DefaultRouter()
router.register('books', views.BookModelViewSet, basename='books')

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('prices/', views.Book.as_view(), name='book')
]

urlpatterns += router.urls
