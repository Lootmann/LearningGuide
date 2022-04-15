# snippets/models.py
import markdown
from django.db import models


class SnippetModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(null=False, blank=True, default="")

    def md_to_html(self):
        md = markdown.Markdown(extensions=["extra", "admonition", "sane_lists", "toc"])
        html = md.convert(self.text)
        return html

    def short_text(self):
        return self.text.split("\n")[0]

    def __str__(self):
        return self.title
