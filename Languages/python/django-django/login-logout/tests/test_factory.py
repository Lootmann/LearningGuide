# tests/test_factory.py
from django.contrib.auth import get_user_model
from django.test import TestCase

from tests import factory


class TestFactoryCustomUser(TestCase):
    def setUp(self) -> None:
        self.user = factory.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
        )

    def test_guest_user(self):
        user = get_user_model().objects.first()
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


class TestFactoryCustomAdminUser(TestCase):
    def setUp(self) -> None:
        self.admin = factory.create_superuser(
            username="testadmin",
            email="testadmin@example.com",
            password="adminpassword123",
        )

    def test_guest_user(self):
        user = get_user_model().objects.first()
        self.assertEqual(user.username, "testadmin")
        self.assertEqual(user.email, "testadmin@example.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
