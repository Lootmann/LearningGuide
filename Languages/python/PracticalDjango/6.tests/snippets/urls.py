from django.urls import path

from snippets.views import SnippetCreateView, SnippetIndexView

app_name = "snippets"

urlpatterns = [
    path("", SnippetIndexView.as_view(), name="index"),
    path("create/", SnippetCreateView.as_view(), name="create"),
]
