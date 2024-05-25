import django_filters
from core import models


class Book(django_filters.FilterSet):
    name = django_filters.CharFilter(label='Название', lookup_expr='icontains')
    date_to = django_filters.DateFilter(label="Дата до", field_name="publication_date", lookup_expr='lt')
    price_from = django_filters.NumberFilter(label="Цена до", field_name="price", lookup_expr='lte')

    class Meta:
        model = models.Book
        exclude = ('picture',)
