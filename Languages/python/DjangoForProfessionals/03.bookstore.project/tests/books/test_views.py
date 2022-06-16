# tests/books/test_views.py
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.test import TestCase
from django.urls import resolve, reverse

from books.models import Book, Review
from books.views import BookListView


class BookListViewTests(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass123",
        )

        # login
        self.client.login(username="testuser", password="testpass123")

        self.book = Book.objects.create(title="A super book", author="me", price=100.99)
        url = reverse("books:book_list")
        self.response = self.client.get(url)

    def test_indexview_status_code(self):
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

    def test_book_list_view_for_logged_out_user(self):
        self.client.logout()

        response = self.client.get(reverse("books:book_list"))
        self.assertEqual(response.status_code, 302)

        redirect_url = "{}?next=/books/".format(reverse("account_login"))
        self.assertRedirects(response, redirect_url)

        response = self.client.get(redirect_url)
        self.assertEqual(response.status_code, 200)


class TestBookDetailView(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="reviewuser",
            email="review@example.com",
            password="testpass123",
        )

        self.special_permission = Permission.objects.get(codename="special_status")

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

    def test_user_logged_in(self):
        self.assertTrue(self.user.is_authenticated)

    def test_book_detail_view_with_permissions(self):
        self.client.login(email="review@example.com", password="testpass123")
        self.user.user_permissions.add(self.special_permission)

        response = self.client.get(self.book.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Harry Potter")
        self.assertTemplateUsed(response, "books/book_detail.html")

        self.assertContains(response, "An excellent review")
        self.assertContains(response, "reviewuser")
        self.assertTemplateUsed(response, "books/book_detail.html")
