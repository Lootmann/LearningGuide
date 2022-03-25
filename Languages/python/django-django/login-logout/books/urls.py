# books/urls.py
from django.urls import path

from books.views import BookIndexView, BookCreateView

app_name = "books"

urlpatterns = [
    path("", BookIndexView.as_view(), name="index"),
    path("create/", BookCreateView.as_view(), name="create"),
]
