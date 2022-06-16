# books/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

from books.models import Book


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    context_object_name = "books"
    template_name = "books/book_list.html"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, generic.DetailView):
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    login_url = "account_login"
    permission_required = "books.special_status"
