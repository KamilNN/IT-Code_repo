from django.test import Client
from rest_framework.test import APITestCase
from core import models


class Tests(APITestCase):
    def setUp(self):
        self.client = Client()
        self.book = models.Book.objects.create(
            name='Война и мир',
            publication_date=1869,
            author='Лев Толстой',
            price=300,
        )

    def test_list(self) -> None:
        response = self.client.get('/books/')
        self.assertEquals(response.status_code, 200)

    def test_detail(self) -> None:
        response = self.client.get('/books/5/')
        self.assertEquals(response.status_code, 200)

    def test_create(self) -> None:
        data = {
            'name': 'Старик и море',
            'author': 'Эрнест Хемингуэй',
            'publication_date': 1952,
            'price': 400,
        }
        response = self.client.post('/books/6/', data)
        self.assertEquals(response.status_code, 201)

    def test_update(self) -> None:
        data = {
            'publication_date': 1869,
            'price': 300,
        }
        response = self.client.put('/books/5/', data)
        self.assertEquals(response.status_code, 200)

    def test_partial_update(self) -> None:
        data = {"price": 800}
        response = self.client.patch('/books/5', data)
        self.assertEquals(response.status_code, 200)

    def test_delete(self) -> None:
        response = self.client.delete('/books/5')
        self.assertEquals(response.status_code, 204)
