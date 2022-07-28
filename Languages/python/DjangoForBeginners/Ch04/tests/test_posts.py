# tests/test_posts.py
from django.test import TestCase
from django.urls import reverse
from pytest_django import asserts

from posts.models import Post


class PostModelTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text="just a test")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f"{post.text}"
        assert expected_object_name == "just a test"


class HomePageViewTest(TestCase):
    def setUp(self) -> None:
        Post.objects.create(text="this is another test")

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get("/posts/")
        assert response.status_code == 200

    def test_view_url_by_name(self):
        response = self.client.get(reverse("posts:home"))
        assert response.status_code == 200

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("posts:home"))
        assert response.status_code == 200
        asserts.assertTemplateUsed(response, "posts/home.html")
