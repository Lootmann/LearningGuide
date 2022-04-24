# tests/test_account.py
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tests.factory import create_user


class TestAccountSignUpView(TestCase):
    def setUp(self) -> None:
        self.url = reverse("accounts:signup")

    def test_create_new_user(self):
        credentials = {
            "username": "test_user",
            "email": "test@example.com",
            "password1": "testpass123",
            "password2": "testpass123",
        }

        response = self.client.post(self.url, credentials)

        self.assertRedirects(response, reverse("accounts:login"))
        user = get_user_model().objects.first()

        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")


class TestAccountLogout(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        self.user = create_user(
            username="test_user", email="test@example.com", password="test_password123"
        )

        credentials = {
            "username": "test_user",
            "email": "test@example.com",
            "password": "test_password123",
        }

        self.c.login(**credentials)

    def test_login(self):
        self.assertTrue(self.user.is_authenticated)

    def test_logout(self):
        response = self.c.post(reverse("accounts:logout"))
        self.assertRedirects(response, reverse("accounts:login"))
