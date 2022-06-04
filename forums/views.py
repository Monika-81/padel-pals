from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Topic, Post, Comments
from .forms import CommentsForm, PostForm


class TopicList(generic.ListView):
    model = Topic
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(TopicList, self).get_context_data(**kwargs)
        return context


class TopicDisplay(View):

    def get(self, request, topic, *args, **kwargs):
        queryset = Topic.objects
        topic = get_object_or_404(queryset, topic=topic)
        posts = topic.topic_posts.order_by('-created_date')

        return render(
            request,
            'topic.html',
            {
                "posts": posts
            },
        )


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.order_by('-created_date')
#     template_name = 'index.html'
#     paginate_by = 10


class PostDisplay(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
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
                'commented': False,
                'liked': liked,
                'comment_form': CommentsForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by("created_date")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentsForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.generator = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_display', args=[slug]))
            
        else:
            comment_form = CommentsForm()

        return render(
            request,
            "thread.html",
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
                'liked': liked
            },
        )


class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_display', args=[slug]))



class AddPost(View):

    def get(self, request):
        return render(
            request, 
            "post_form.html",
            {
                "post_form": PostForm()
            },
        )

    def post(self, request):
        post_form = PostForm(request.POST, request.FILES)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.generator = request.user
            post.slug = slugify(post.title, allow_unicode=False)
            post.save()
            return redirect('home')
        else:
            post_form = PostForm()

        context = {'form': post_form}
        return render(
            request, 
            'post_form.html',
            context
            )
