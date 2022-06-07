from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, View, UpdateView
from django.http import HttpResponseRedirect
from django.utils.text import slugify
from .models import Topic, Post, Comments
from .forms import CommentsForm, PostForm, ContactForm


# Topics
class TopicList(ListView):
    model = Topic
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TopicList, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_date')
        return context


class TopicDisplay(View):

    def get(self, request, topic, *args, **kwargs):
        queryset = Topic.objects
        topic = get_object_or_404(queryset, topic=topic)
        posts = topic.topic_posts.order_by('-created_date')
        topics = Topic.objects.all()

        return render(
            request,
            'topic.html',
            {
                "topic_list": topics,
                "posts": posts
            },
        )


# Posts
class PostDisplay(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_date')
        topics = Topic.objects.all()

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            'thread.html',
            {
                "topic_list": topics,
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


# Like posts
class PostLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_display', args=[slug]))


# Add posts
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
        post_form = PostForm(request.POST)

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

# Edit Posts
class EditPost(UpdateView):
    model = Post
    template_name = "edit_post.html"
    fields = ['topic', 'title', 'content']


def deletePost(request, slug):

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect(reverse(
        'home'))


# Edit Comments
class EditComment(UpdateView):
    model = Comments
    template_name = 'edit_comment.html'
    form_class = CommentsForm


def deleteComment(request, comments_id):

    comments = get_object_or_404(Comments, id=comments_id)
    comments.delete()
    return HttpResponseRedirect(reverse(
        'post_display', args=[comments.post.slug]))


# Users Posts
class UserPosts(View):

    def get(self, request):
        if request.user.is_authenticated:
            posts = Post.objects.filter(generator=request.user)

            return render(
                request,
                'user_posts.html',
                {
                    "posts": posts
                }
            )

        else:
            return render(
                request,
                'user_posts.html')


# Searchbar
class Search(View):

    def get(self, request):
        return render(
            request, 
            'search.html',
        )  

    def post(self, request):

        if request.method == 'POST':
            search = request.POST.get('search')
            posts = Post.objects.filter(title__contains=search)

            context = {
                'search': search,
                'posts': posts,
            }

            return render(request, 'search.html', context)
        else:
            return render(request, 'search.html')


# Contactform
class Contact(View):

    def get(self, request, *args, **kwargs):

        return render(
            request,
            'contact.html',
            {
                'contact': ContactForm()
            }
        )
    
    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            return redirect('home')
        else:
            contact_form = PostForm()

        return render(
            request, 
            'contact.html',
            {
                'contact': ContactForm()
            }
        )

