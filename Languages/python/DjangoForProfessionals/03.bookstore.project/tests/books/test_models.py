# tests/books/test_models.py
from django.test import TestCase

from books.models import Book


class TestBookModel(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )

    def test_book_listing(self):
        self.assertEqual(f"{self.book.title}", "Harry Potter")
        self.assertEqual(f"{self.book.author}", "JK Rowling")
        self.assertEqual(f"{self.book.price}", "25.00")
