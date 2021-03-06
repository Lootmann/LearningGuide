# tests/test_book.py
from django.test import TestCase
from django.urls import reverse

from books.models import BookModel
from tests import factory


class TestBookModel(TestCase):
    def setUp(self) -> None:
        self.book = BookModel.objects.create(name="testbook")

    def test_book_model(self):
        self.assertEqual(self.book.name, "testbook")

    def test_book_model_str(self):
        self.assertEqual(str(self.book), "testbook")


class TestBookIndexView(TestCase):
    def setUp(self) -> None:
        self.url = reverse("books:index")
        self.response = self.client.get(self.url)

    def test_index_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_index_view_template(self):
        self.assertTemplateUsed(self.response, "base.html")
        self.assertTemplateUsed(self.response, "books/index.html")

    def test_index_view_url(self):
        self.assertEqual(self.url, "/")


class TestBookCreateViewWithoutLogin(TestCase):
    def setUp(self) -> None:
        self.client.logout()
        self.url = reverse("books:index")
        self.response = self.client.get(self.url)

    def test_create_view_post_without_login(self):
        """
        BookCreateView redirects /accounts/login/ when user is not logged int
        """
        redirect_url = self.client.post(
            reverse("books:create"),
            {
                "name": "testbook",
            },
        )

        self.assertRedirects(redirect_url, "/accounts/login/?next=/create/")


class TestBookCreateViewWithLogin(TestCase):
    def setUp(self) -> None:
        user = factory.create_user(
            username="testuser", email="testemail@example.com", password="testpassword123"
        )
        self.client.force_login(user)

    def test_book_model_has_no_record(self):
        self.assertEqual(BookModel.objects.count(), 0)

    def test_book_create_view(self):
        redirect_url = self.client.post(
            reverse("books:create"),
            {"name": "testbook"},
        )
        self.assertRedirects(redirect_url, reverse("books:index"))

        self.assertEqual(BookModel.objects.count(), 1)
        self.assertEqual(BookModel.objects.first().name, "testbook")


class TestBookLoginTemplate(TestCase):
    def setUp(self) -> None:
        self.client.logout()

        self.url = reverse("books:index")
        self.response = self.client.get(self.url)

    def test_login_template_without_login(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "books/index.html")
        self.assertContains(self.response, "You Don't Login")
        self.assertContains(self.response, "Login")
        self.assertContains(self.response, "SignUp")

    def test_login_template_with_login(self):
        user = factory.create_user(
            username="testuser", email="testuser@example.com", password="testpassword123"
        )

        # login
        # self.client.login(username=user.username, password="testpassword123")
        self.client.force_login(user)

        response = self.client.get(reverse("books:index"))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, "books/index.html")
        self.assertContains(response, "book.index")
        self.assertContains(response, "book.create")
        self.assertContains(response, "Logout")
