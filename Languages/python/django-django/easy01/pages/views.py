# pages/views.py
from django.views import generic


class PagesIndexView(generic.TemplateView):
    template_name = "pages/index.html"
