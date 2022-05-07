from django.test import SimpleTestCase
from django.urls import resolve, reverse

from pages.views import PagesIndexView


class PagesIndexViewTests(SimpleTestCase):
    def setUp(self):
        url = reverse("pages:index")
        self.response = self.client.get(url)

    def test_indexview_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_indexview_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_indexpage_template_used(self):
        self.assertTemplateUsed(self.response, "pages/index.html")

    def test_index_contains_correct_html(self):
        self.assertContains(self.response, "pages/index.html")

    def test_index_does_not_contain_correct_html(self):
        self.assertNotContains(self.response, "index/pages.html")

    def test_index_page_url_resolves_index_view(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            PagesIndexView.as_view().__name__,
        )
