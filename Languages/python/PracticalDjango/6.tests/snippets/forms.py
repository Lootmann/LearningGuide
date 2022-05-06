from django import forms

from snippets.models import SnippetModel


class SnippetCreateForms(forms.ModelForm):
    class Meta:
        model = SnippetModel
        fields = ("title", "code", "description")
