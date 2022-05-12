from django.test import SimpleTestCase
from django.urls import resolve, reverse

from pages.views import PagesIndexView, PagesAboutView


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


class PagesAboutViewTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("pages:about")
        self.response = self.client.get(url)

    def test_aboutpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_aboutpage_template(self):
        self.assertTemplateUsed(self.response, "pages/about.html")

    def test_aboutpage_contains_correct_html(self):
        self.assertContains(self.response, "pages/about.html")

    def test_aboutpage_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "About Page")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            PagesAboutView.as_view().__name__,
        )
