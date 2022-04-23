# snippets/views.py
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods

from snippets.forms import SnippetForm
from snippets.models import Snippet


@require_safe
def top(request: HttpRequest):
    snippets = Snippet.objects.all()
    context = {"snippets": snippets}
    return render(request, "snippets/top.html", context)


@require_http_methods(["GET", "POST", "HEAD"])
@login_required
def snippet_new(request: HttpRequest):
    if request.method == "POST":
        form = SnippetForm(request.POST)

        if form.is_valid:
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            return redirect("snippet_detail", snippet_id=snippet.id)

    form = SnippetForm()
    return render(request, "snippets/snippet_new.html", {"form": form})


@login_required
def snippet_edit(request: HttpRequest, snippet_id: int):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    if snippet.created_by_id != request.user.id:
        return HttpResponseForbidden("This snippet cannot be allowed edited.")

    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            return redirect("snippet_detail", snippet_id=snippet_id)
        else:
            form = SnippetForm(instance=snippet)
        return render(request, "snippets/snippet_edit.html", {"form": form})


def snippet_detail(request: HttpRequest, snippet_id: int):
    snippet = get_object_or_404(Snippet, pk=snippet_id)
    return render(request, "snippets/snippet_detail.html", {"snippet": snippet})
