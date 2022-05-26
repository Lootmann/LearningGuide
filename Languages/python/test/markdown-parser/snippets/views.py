# snippets/views.py
from django.urls import reverse_lazy
from django.views import generic

from snippets.models import SnippetModel


class SnippetsIndexView(generic.ListView):
    model = SnippetModel
    template_name = "snippets/index.html"
    context_object_name = "snippets"


class SnippetsCreateView(generic.CreateView):
    model = SnippetModel
    fields = ("title", "code")
    template_name = "snippets/create.html"

    def get_success_url(self):
        print(self.kwargs)
        return reverse_lazy("snippets:detail", kwargs={"pk": self.object.id})


class SnippetsDetailView(generic.DetailView):
    model = SnippetModel
    template_name = "snippets/detail.html"
    context_object_name = "snippet"
