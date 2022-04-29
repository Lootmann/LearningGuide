# snippets/models.py
from django.db import models


class Snippet(models.Model):
    class Meta:
        db_table = "snippets"
        verbose_name = "snippet"
        verbose_name_plural = "snippets"

    title = models.CharField("Title", max_length=128, null=False, blank=False)
    code = models.TextField("Code", null=False, blank=True)
    description = models.TextField("Description", blank=True)
    created_at = models.DateTimeField("PostedAt", auto_now_add=True)
    updated_at = models.DateTimeField("UpdatedAt", auto_now=True)


class Comment(models.Model):
    class Meta:
        db_table = "comments"

    text = models.TextField("Sentence", blank=False)
    commented_to = models.ForeignKey(
        Snippet,
        verbose_name="snippet",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return f"{self.pk} {self.text}"


class Tag(models.Model):
    class Meta:
        db_table = "tags"

    name = models.CharField("TagName", max_length=32)
    snippets = models.ManyToManyField(
        Snippet,
        related_name="tags",
        related_query_name="tag",
    )

    def __str__(self) -> str:
        return f"{self.pk} {self.name}"
