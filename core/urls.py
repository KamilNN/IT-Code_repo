from django.urls import path
from .views import *
from .views import BookView


urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('book/<int:id>/<str:name>/', BookView.as_view(), name='book')
]
