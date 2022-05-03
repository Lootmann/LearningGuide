from django import forms

from snippets.models import Snippet


class SnippetForms(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("title", "code", "description")

    def form_valid(self, form):
        print(form)
        return super().form_valid(form)
