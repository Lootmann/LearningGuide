# books/urls.py
from django.urls import path

from books.views import BookDetailView, BookListView

app_name = "books"

urlpatterns = [
    path("", BookListView.as_view(), name="book_list"),
    path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
]
