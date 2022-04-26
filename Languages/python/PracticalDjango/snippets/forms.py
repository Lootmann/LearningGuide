# snippets/forms.py
from django import forms

from snippets.models import Snippet, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)


class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("title", "code", "description")
