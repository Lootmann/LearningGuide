from django.urls import reverse_lazy
from django.views import generic

from snippets.forms import SnippetCreateForms
from snippets.models import SnippetModel


class SnippetIndexView(generic.ListView):
    model = SnippetModel
    template_name = "snippets/index.html"
    context_object_name = "snippets"


class SnippetCreateView(generic.CreateView):
    model = SnippetModel
    form_class = SnippetCreateForms
    template_name = "snippets/create.html"
    success_url = reverse_lazy("snippets:index")
