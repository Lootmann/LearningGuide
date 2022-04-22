# snippets/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect, get_object_or_404

from snippets.forms import SnippetForm
from snippets.models import Snippet


def top(request: HttpRequest):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, "snippets/top.html", context)


@login_required
def snippet_new(request: HttpRequest):
    if request.method == "POST":
        form = SnippetForm(request.POST)

        if form.is_valid:
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect(snippet_detail, id=snippet.id)

    form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {"form": form})


@login_required
def snippet_edit(request: HttpRequest, snippet_id: int):
    return HttpResponse("edit snippets")


def snippet_detail(request: HttpRequest, snippet_id: int):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, "snippets/snippet_detail.html", {"snippet": snippet})
