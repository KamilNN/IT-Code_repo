from django.db import models
from django.db.models import CharField


class Book(models.Model):

    TYPE_CHOICES = (
        ('science-fiction', 'Научная фантастика'),
        ('adventure', 'Приключения'),
        ('horror', 'Ужасы'),
    )
    publication_date = models.DateField('Дата публикации')
    name = models.CharField('Название', max_length=40)
    author = models.CharField('Автор', max_length=40, default='Неизвестно')
    genre = models.CharField('Жанр', max_length=40, choices=TYPE_CHOICES, default='Неизвестно')
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена книги', max_digits=5, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self) -> CharField:
        return self.name


class Building(models.Model):
    name = models.CharField('Название', max_length=40, default='Без названия')
    height = models.IntegerField('Высота')
    architector = models.CharField('Архитектор', max_length=40, default='Неизвестно')
    foundation_date = models.DateField('Дата основания')
    picture = models.ImageField('Фото здания', upload_to='pictures', blank=True)
    is_world_heritage = models.BooleanField('Объект всемрного наследия', default=False)

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"

    def __str__(self) -> CharField:
        return self.name
