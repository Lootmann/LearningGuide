# snippets/models.py

from django.conf import settings
from django.db import models


class Comment(models.Model):
    comment = models.TextField()

    commented_to = models.ForeignKey("Snippet", on_delete=models.CASCADE)
    commented_at = models.DateTimeField("CommentedAt", auto_now_add=True)
    commented_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="PostedBy",
        on_delete=models.CASCADE,
    )


class Snippet(models.Model):
    title = models.CharField("Title", max_length=128)
    code = models.TextField("Code", blank=True)
    description = models.TextField("Description", blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="PostedBy",
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField("CreatedAt", auto_now_add=True)
    updated_at = models.DateTimeField("UpdatedAt", auto_now=True)

    def __str__(self) -> str:
        return self.title
