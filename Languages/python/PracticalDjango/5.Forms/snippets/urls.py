from django.urls import path

from snippets.views import SnippetCreate, SnippetIndex


app_name = "snippets"

urlpatterns = [
    path("", SnippetIndex.as_view(), name="index"),
    path("create/", SnippetCreate.as_view(), name="create"),
]
