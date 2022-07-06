# books/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
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


class BookSearchListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        query = self.request.GET["q"]
        return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
