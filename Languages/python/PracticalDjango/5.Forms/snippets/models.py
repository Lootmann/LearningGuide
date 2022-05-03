from django.db import models


class Snippet(models.Model):
    title = models.CharField("Title", max_length=128)
    code = models.TextField("Code", blank=True)
    description = models.TextField("Description", blank=True)
