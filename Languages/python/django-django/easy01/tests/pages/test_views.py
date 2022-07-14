# tests/pages/test_views.py
from django.test import TestCase
from django.urls import reverse, resolve
from pytest_django import asserts

from pages.views import PagesIndexView


class TestPagesIndexView(TestCase):
    def setUp(self) -> None:
        self.url = reverse("pages:index")
        self.response = self.client.get(self.url)

    def test_status_code(self):
        assert self.response.status_code == 200

    def test_templates_used(self):
        asserts.assertTemplateUsed(self.response, "base.html")
        asserts.assertTemplateUsed(self.response, "pages/index.html")

    def test_contains(self):
        asserts.assertContains(self.response, "pages/index")

    def test_pages_indexview_resolve_view(self):
        view = resolve("/pages/")
        self.assertEqual(
            view.func.__name__,
            PagesIndexView.as_view().__name__,
        )
