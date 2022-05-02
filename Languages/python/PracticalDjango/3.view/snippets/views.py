from django.urls import reverse_lazy
from django.views import generic

from snippets.models import Snippet


class SnippetIndexCiew(generic.ListView):
    model = Snippet
    template_name = "snippets/index.html"
    context_object_name = "snippets"


class SnippetCreateView(generic.CreateView):
    model = Snippet
    template_name = "snippets/create.html"
    fields = ("title", "code")
    successful_url = reverse_lazy("snippets:index")


class SnippetDetailView(generic.DeleteView):
    model = Snippet
    template_name = "snippets/detail.html"
    context_objects_name = "snippet"
