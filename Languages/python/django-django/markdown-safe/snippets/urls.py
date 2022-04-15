# snippets/urls.py
from django.urls import path

from snippets.views import (
    SnippetIndexView,
    SnippetCreateView,
    SnippetDetailView,
    SnippetUpdateView,
)

app_name = "snippets"

urlpatterns = [
    path("", SnippetIndexView.as_view(), name="index"),
    path("create/", SnippetCreateView.as_view(), name="create"),
    path("detail/<int:pk>/", SnippetDetailView.as_view(), name="detail"),
    path("update/<int:pk>/", SnippetUpdateView.as_view(), name="update"),
]
