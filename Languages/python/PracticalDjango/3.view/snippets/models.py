from django.db import models
from django.urls import reverse


class Snippet(models.Model):
    title = models.CharField("Title", max_length=128)
    code = models.TextField("Code")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("snippet:detail", kwargs={"pk": self.pk})

    def short_code(self):
        return self.code.split("\n")[0]
