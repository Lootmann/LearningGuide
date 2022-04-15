# snippets/views.py
from django.urls import reverse_lazy
from django.views import generic

from snippets.models import SnippetModel


class SnippetIndexView(generic.ListView):
    model = SnippetModel
    context_object_name = "snippets"
    template_name = "snippets/index.html"


class SnippetCreateView(generic.CreateView):
    model = SnippetModel
    template_name = "snippets/create.html"
    fields = ("title", "text")
    success_url = reverse_lazy("snippets:index")


class SnippetDetailView(generic.DetailView):
    model = SnippetModel
    template_name = "snippets/detail.html"
    context_object_name = "snippet"
    fields = ("title", "text")


class SnippetUpdateView(generic.UpdateView):
    model = SnippetModel
    template_name = "snippets/update.html"
    context_object_name = "snippet"
    fields = ("title", "text")

    def get_success_url(self):
        return reverse("snippets:detail", kwargs={"pk": self.kwargs["pk"]})
