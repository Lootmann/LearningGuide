# posts/views.py
from django.views import generic

from posts.models import Post


class HomePageView(generic.ListView):
    model = Post
    template_name = "posts/home.html"
    context_object_name = "all_posts_lists"
