# snippets/urls.py
from django.urls import path

from snippets.views import SnippetsIndexView, SnippetsCreateView, SnippetsDetailView

app_name = "snippets"

urlpatterns = [
    path("", SnippetsIndexView.as_view(), name="index"),
    path("create/", SnippetsCreateView.as_view(), name="create"),
    path("detail/<uuid:pk>/", SnippetsDetailView.as_view(), name="detail"),
]
