# quiz/forms.py
from django import forms

from quiz.models import QuizModel


class QuizCreateForm(forms.ModelForm):
    class Meta:
        model = QuizModel
        fields = ("statement", "answer")
