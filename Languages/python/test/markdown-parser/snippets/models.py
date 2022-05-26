# snippets/models.py
import uuid

from django.db import models


class SnippetModel(models.Model):
    id = models.UUIDField(
        "snippet_id",
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    title = models.CharField(
        "Title",
        max_length=128,
        null=False,
        blank=False,
    )

    code = models.TextField(
        "Code",
        null=False,
        blank=True,
    )

    def code_heading(self) -> str:
        return self.code.split("\n")[0][:40]

    def __str__(self) -> str:
        return self.title
