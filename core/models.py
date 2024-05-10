from django.db import models
from django.shortcuts import reverse
from django.db.models import CharField


class Book(models.Model):
    objects = models.Manager()

    publication_date = models.DateField('Дата публикации')
    name = models.CharField('Название', max_length=40)
    author = models.CharField('Автор', max_length=40, default='Неизвестно')
    description = models.TextField('Описание', blank=True)
    picture = models.ImageField('Фото обложки', upload_to='pictures', blank=True)
    price = models.DecimalField('Цена книги', max_digits=5, decimal_places=2, default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Категория', null=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self) -> CharField:
        return self.name

    def get_absolute_url(self):
        return reverse('book', kwargs={'id': self.pk, 'name': self.name})


class Category(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=50, db_index=True, verbose_name='Категория')

    def __str__(self) -> CharField:
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


# class Building(models.Model):
#     name = models.CharField('Название', max_length=40, default='Без названия')
#     height = models.IntegerField('Высота')
#     architector = models.CharField('Архитектор', max_length=40, default='Неизвестно')
#     foundation_date = models.DateField('Дата основания')
#     picture = models.ImageField('Фото здания', upload_to='pictures', blank=True)
#     is_world_heritage = models.BooleanField('Объект всемрного наследия', default=False)
#
#     class Meta:
#         verbose_name = "Здание"
#         verbose_name_plural = "Здания"
#
#     def __str__(self) -> CharField:
#         return self.name
