from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import resolve, reverse

from accounts.forms import CustomUserCreationForm
from accounts.views import SignupPageView

UserModel = get_user_model()


class CustomUserTests(TestCase):
    def setUp(self):
        pass

    def test_create_user(self):
        user = UserModel.objects.create_user(
            username="will",
            email="will@example.com",
            password="testpass123",
        )

        self.assertEqual(user.username, "will")
        self.assertEqual(user.email, "will@example.com")

        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_supseruser(self):
        admin_user = UserModel.objects.create_superuser(
            username="superuser",
            email="superuser@example.com",
            password="testpass123",
        )
        self.assertEqual(admin_user.username, "superuser")
        self.assertEqual(admin_user.email, "superuser@example.com")

        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)


class SignupPageTests(TestCase):
    def setUp(self):
        url = reverse("signup")
        self.response = self.client.get(url)

    def test_signup_templates(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, "registration/signup.html")
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Login")

    def test_signup_form(self):
        form = self.response.context.get("form")
        self.assertIsInstance(form, CustomUserCreationForm)
        self.assertContains(self.response, "Sign Up")
        self.assertContains(self.response, "csrfmiddlewaretoken")

    def test_signup_view(self):
        view = resolve("/accounts/signup/")
        self.assertEqual(
            view.func.__name__,
            SignupPageView.as_view().__name__,
        )
