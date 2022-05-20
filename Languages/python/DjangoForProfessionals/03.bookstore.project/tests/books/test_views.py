from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse

from books.models import Book
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
