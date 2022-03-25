# books/views.py
from django.urls import reverse_lazy
from django.views import generic

from books.models import BookModel


class BookIndexView(generic.ListView):
    model = BookModel
    template_name = "books/index.html"
    context_object_name = "books"


class BookCreateView(generic.CreateView):
    model = BookModel
    template_name = "books/create.html"
    fields = ("name",)
    success_url = reverse_lazy("books:index")
