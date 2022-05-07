from django.views.generic import TemplateView


class PagesIndexView(TemplateView):
    template_name = "pages/index.html"
