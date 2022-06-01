from django.shortcuts import render
from django.views import generic
from .models import Topic, Post, Comments


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 10

