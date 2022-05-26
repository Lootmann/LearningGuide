# tests/snippets/test_views.py
from django.test import TestCase
from django.urls import reverse

from snippets.models import SnippetModel


class TestSnippetIndexView(TestCase):
    def setUp(self) -> None:
        self.snippet = SnippetModel.objects.create(title="test snippet", code="# hello world")

        self.url = reverse("snippets:index")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "snippets/index.html")

    def test_contains(self):
        self.assertContains(self.response, f"{self.snippet.id}")
        self.assertContains(self.response, "test snippet")
        self.assertContains(self.response, "# hello world")


class TestSnippetCreateView(TestCase):
    def setUp(self) -> None:
        self.url = reverse("snippets:create")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "snippets/create.html")

    def test_post_create_snippet(self):
        data = {"title": "test snippet", "code": "# hello world"}
        response = self.client.post(self.url, data)

        snippet = SnippetModel.objects.first()
        self.assertRedirects(
            response,
            reverse("snippets:detail", kwargs={"pk": snippet.id}),
            status_code=302,
        )


class TestSnippetDetailView(TestCase):
    def setUp(self) -> None:
        self.snippet = SnippetModel.objects.create(title="test snippet", code="#hello world")

        self.url = reverse("snippets:detail", kwargs={"pk": self.snippet.id})
        self.response = self.client.get(self.url)

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, "snippets/detail.html")

    def test_contains(self):
        self.assertContains(self.response, f"{self.snippet.id}")
        self.assertContains(self.response, f"{self.snippet.title}")
        self.assertContains(self.response, f"{self.snippet.code}")
