# tests/books/test_views.py
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from books.models import Book, Review
from books.views import BookListView


class BookListViewTests(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title="A super book", author="me", price=100.99)
        url = reverse("books:book_list")
        self.response = self.client.get(url)

    def test_indexview_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_indexview_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_indexpage_template_used(self):
        self.assertTemplateUsed(self.response, "books/book_list.html")

    def test_index_contains_correct_html(self):
        self.assertContains(self.response, self.book.title)

    def test_index_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "brooklin/list.html")

    def test_index_page_url_resolves_index_view(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            BookListView.as_view().__name__,
        )

    def test_book_list_view(self):
        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A super book")
        self.assertContains(response, "me")
        self.assertTemplateUsed(response, "books/book_list.html")


class TestBookDetailView(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="review@exmaple.com",
            password="testpass123",
        )

        self.book = Book.objects.create(
            title="Harry Potter",
            author="JK Rowling",
            price="25.00",
        )

        self.review = Review.objects.create(
            book=self.book,
            author=self.user,
            review="An excellent review",
        )

        self.response = self.client.get(self.book.get_absolute_url())

    def test_book_detail_view(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertContains(self.response, "Harry Potter")
        self.assertTemplateUsed(self.response, "books/book_detail.html")

    def test_book_detail_view_has_reviews(self):
        self.assertContains(self.response, "An excellent review")
        self.assertContains(self.response, "reviewuser")
        self.assertTemplateUsed(self.response, "books/book_detail.html")
