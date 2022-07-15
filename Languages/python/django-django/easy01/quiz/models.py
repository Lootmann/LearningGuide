# quiz/models.py
from django.db import models


class QuizModel(models.Model):
    statement = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.statement
