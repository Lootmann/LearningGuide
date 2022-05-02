from django.urls import path

from snippets.views import SnippetCreateView, SnippetDetailView, SnippetIndexCiew

app_name = "snippet"

urlpatterns = [
    path("", SnippetIndexCiew.as_view(), name="index"),
    path("create/", SnippetCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", SnippetDetailView.as_view(), name="detail"),
]
