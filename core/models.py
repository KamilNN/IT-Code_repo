from django.db import models


class Book(models.Model):
    publication_date = models.DateField()
    name = models.CharField(max_length=40)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class Building(models.Model):
    height = models.IntegerField()
    architector = models.CharField(max_length=40)
    foundation_date = models.DateField()

    class Meta:
        verbose_name = "Здание"
        verbose_name_plural = "Здания"
