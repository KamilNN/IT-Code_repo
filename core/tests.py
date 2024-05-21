from django.test import TestCase
from django.test import Client
from core import models


class Tests(TestCase):
    def setUp(self):
        self.client = Client()
        self.book = models.Book.objects.create(
            name='Война и мир',
            publication_date=1869,
            author='Лев Толстой',
            price=300,
        )

    def test_index(self):
        response = self.client.get('/index_class/')
        self.assertEquals(response.status_code, 200)

    def test_book_list(self):
        response = self.client.get('/book_list/')
        self.assertEquals(response.status_code, 200)

    def test_book_view(self):
        response = self.client.get(f'/book/{self.book.id}/')
        self.assertEquals(response.status_code, 200)

    def test_redirect(self):
        response = self.client.get('/redirect/')
        self.assertEquals(response.status_code, 302)

    def test_forms(self):
        response = self.client.get('/forms/')
        self.assertEquals(response.status_code, 200)
