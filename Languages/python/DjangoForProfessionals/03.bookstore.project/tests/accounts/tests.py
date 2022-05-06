from django.contrib.auth import get_user_model
from django.test import TestCase

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
