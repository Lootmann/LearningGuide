# blog/views.py
from django.views import generic

from blog.models import Post


class BlogListView(generic.ListView):
    model = Post
    template_name = "blog/home.html"
