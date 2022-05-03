from django.urls import reverse_lazy
from django.views import generic

from snippets.forms import SnippetForms
from snippets.models import Snippet


class SnippetIndex(generic.ListView):
    model = Snippet
    template_name = "snippets/index.html"
    context_object_name = "snippets"


class SnippetCreate(generic.CreateView):
    model = Snippet
    form_class = SnippetForms
    template_name = "snippets/create.html"

    def get_success_url(self):
        return reverse_lazy("snippets:index")
