from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import resolve, reverse
from snippets.views import SnippetCreateView

UserModel = get_user_model()


class SnippetCreateViewTests(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = UserModel.objects.create_user(
            username="test-user",
            email="test@example.com",
            password="testpass123",
        )

    def test_should_return_200_if_sending_get_request(self):
        request = self.factory.get(reverse("snippets:create"))
        request.user = self.user
        response = SnippetCreateView.as_view()(request)
        print(response)
        self.assertEqual(response.status_code, 200)
