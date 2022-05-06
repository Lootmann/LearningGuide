from django.db import models


class SnippetModel(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    code = models.CharField(max_length=128, null=False, blank=False)
    description = models.TextField(null=False, blank=False)

    def __str__(self) -> str:
        return str(self.title)
