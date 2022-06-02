from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Topic, Post, Comments


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.order_by('-created_date')
    template_name = 'index.html'
    paginate_by = 10


class PostDisplay(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_date')

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'thread.html',
            {
                'post': post,
                'comments': comments,
                'liked': liked
            }
        )
