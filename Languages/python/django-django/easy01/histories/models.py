# histories/models.py
from django.db import models

from quiz.models import QuizModel


class HistoryModel(models.Model):
    quiz = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    solved_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("quiz",)

    def __str__(self) -> str:
        return str(self.quiz)
