# tests/tests.py
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        assert response.status_code == 200

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        assert response.status_code == 200
