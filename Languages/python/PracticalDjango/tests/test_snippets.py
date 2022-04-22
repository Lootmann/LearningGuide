# tests/test_snippets.py
from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import resolve

from snippets.models import Snippet
from snippets.views import top, snippet_edit
from tests.factory import create_user

UserModel = get_user_model()


class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = create_user(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass001",
        )

        self.snippet = Snippet.objects.create(
            title="Dango Snippet",
            code="print('Hello World')",
            description="test description",
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)


class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Django Snippet", status_code=200)

    def test_top_page_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "snippets/top.html")


class TestSnippetsView(TestCase):
    def setUp(self) -> None:
        pass

    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class CreateSnippetTest(TestCase):
    def setUp(self) -> None:
        self.user = create_user(
            username="test_user",
            email="test@example.com",
            password="top_secret_password",
        )
        self.client.force_login(self.user)

    def test_render_creation_form(self):
        response = self.client.get("/snippets/new/")
        self.assertContains(response, "", status_code=200)

    def test_create_snippet(self):
        data = {
            "title": "django title",
            "code": "print(123)",
            "description": "description",
        }
        self.client.post("snippets/new/", data)

        snippet = Snippet.objects.get(title="django title")
        self.assertEqual("print(123)", snippet.code)
        self.assertEqual("description", snippet.description)


class SnippetDetailTest(TestCase):
    def setUp(self) -> None:
        self.user = create_user(
            username="test_user",
            email="test@example.com",
            password="test_user_secret_password",
        )

        self.snippet = Snippet.objects.create(
            title="test title",
            code="test code",
            description="test description",
            created_by=self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response, "snippets/snippet_detail.html")

    def test_top_page_results_200_and_expected_heading(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)
        self.assertContains(response, self.snippet.code, status_code=200)


class EditDetailTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, found.func)
