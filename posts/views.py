from django.views.generic import ListView, DetailView

from .models import post


class PostListView(ListView):
    model = post
    paginate_by = 10


class PostDetailView(DetailView):
    model = post
