from django.test import TestCase


class TestSnippet(TestCase):
    def setUp(self):
        print("hello world")

    def test_boom(self):
        self.assertEqual(1, 1)
