from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import ListView, View, UpdateView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.utils.crypto import get_random_string
from django.contrib import messages
from .models import Topic, Post, Comments, Play, PlayComments
from .forms import CommentsForm, PostForm, ContactForm
from .forms import PlayForm, PlayCommentsForm


class TopicList(ListView):
    '''
    View to render the topics nav
    '''
    model = Topic
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(TopicList, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_date')
        return context


class TopicDisplay(View):
    '''
    View to render the posts in a specific topic, orded by date created on
    and paginated to 4 posts per page. Also renders view on topics nav
    '''
    def get(self, request, topic, *args, **kwargs):
        queryset = Topic.objects.all()
        topic = get_object_or_404(queryset, topic=topic)
        posts = topic.topic_posts.order_by('-created_date')
        topics = Topic.objects.all()

        paginator = Paginator(topic.topic_posts.order_by('-created_date'), 4)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(
            request,
            'topic.html',
            {
                "topic_list": topics,
                "posts": posts,
                'page_obj': page_obj
            },
        )


class PostDisplay(View):
    '''
    View to render the details of the selected post
    and it's comments and likes
    '''
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
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your comment was submitted!'
                )
            return HttpResponseRedirect(reverse('post_display', args=[slug]))

        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Invalid submit, please fill out all the required fields!'
                )
            return HttpResponseRedirect(reverse('post_display', args=[slug]))

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
    '''
    View to let a user like or unlike a post
    '''
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_display', args=[slug]))


class AddPost(View):
    '''
    View to allow a new post to be added
    '''
    def get(self, request):
        topics = Topic.objects.all()
        return render(
            request,
            "post_form.html",
            {
                "topic_list": topics,
                "post_form": PostForm()
            },
        )

    def post(self, request):
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.generator = request.user
            post.slug = get_random_string(8, '0123456789')
            post.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your post was submitted!'
                )
            return redirect('home')
        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Invalid submit, please fill out all the required fields!'
                )
            return HttpResponseRedirect(reverse('add_post'))

        context = {
            'form': post_form
            }
        return render(
            request,
            'post_form.html',
            context
            )


class EditPost(UpdateView):
    '''
    View to let the user edit a post
    '''
    model = Post
    template_name = "edit_post.html"
    fields = ['topic', 'title', 'content']


def delete_post(request, slug):
    '''
    View to let the user delete a post
    '''
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect(reverse('home'))


class EditComment(UpdateView):
    '''
    View to let the user edit a comment
    '''
    model = Comments
    template_name = 'edit_comment.html'
    form_class = CommentsForm


def delete_comment(request, comments_id):
    '''
    View to let the user delete a comment
    '''
    comments = get_object_or_404(Comments, id=comments_id)
    comments.delete()
    return HttpResponseRedirect(reverse(
        'post_display', args=[comments.post.slug]))


class Search(View):
    '''
    View to render the search results from the searchbar
    '''
    def get(self, request):
        return render(
            request,
            'search.html',
        )

    def post(self, request):

        if request.method == 'POST':
            search = request.POST.get('search')
            posts = Post.objects.filter(title__contains=search)
            plays = Play.objects.filter(description__contains=search)
            contents = Post.objects.filter(content__contains=search)
            topics = Topic.objects.all()

            context = {
                "topic_list": topics,
                'search': search,
                'posts': posts,
                'plays': plays,
                'contents': contents
            }
            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')


class Contact(View):
    '''
    View that allow the sending of a contact form to the admin
    '''
    def get(self, request, *args, **kwargs):
        topics = Topic.objects.all()

        return render(
            request,
            'contact.html',
            {
                "topic_list": topics,
                'contact': ContactForm()
            }
        )

    def post(self, request, *args, **kwargs):
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Contact form sent, we will get back to you shortly!'
                )
            return redirect('home')

        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Invalid submit, please fill out all the required fields!'
                )
            return HttpResponseRedirect(reverse('contact'))

        return render(
            request,
            'contact.html',
            {
                'contact': ContactForm()
            }
        )


class AddPlay(View):
    '''
    View that allows a new play event post to be added
    '''
    def get(self, request):
        topics = Topic.objects.all()
        return render(
            request,
            "play.html",
            {
                "topic_list": topics,
                "play_form": PlayForm()
            },
        )

    def post(self, request):
        play_form = PlayForm(request.POST)

        if play_form.is_valid():
            play = play_form.save(commit=False)
            play.generator = request.user
            play.slug = get_random_string(8, 'abcdefghi')
            play.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your post was submitted!'
                )
            return redirect('play_events')

        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Invalid submit, please fill out all the required fields!'
                )
            return HttpResponseRedirect(reverse('play'))

        context = {'form': play_form}
        return render(
            request,
            'play.html',
            context
            )


class PlayEventsList(ListView):
    '''
    View that render a list of play event posts
    '''
    def get(self, request):
        plays = Play.objects.all()
        topics = Topic.objects.all()

        return render(
            request,
            'play_list.html',
            {
                "topic_list": topics,
                "play_list": plays
            }
        )


class PlayEventsDisplay(View):
    '''
    View to render the details of a play event
    '''
    def get(self, request, slug, *args, **kwargs):
        queryset = Play.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.play_list_comments.order_by('created_date')
        topics = Topic.objects.all()

        return render(
            request,
            'play_display.html',
            {
                "topic_list": topics,
                'post': post,
                'comments': comments,
                'commented': False,
                'comment_form': PlayCommentsForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Play.objects.all()
        post = get_object_or_404(queryset, slug=slug)
        comments = post.play_list_comments.order_by('created_date')

        comment_form = PlayCommentsForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.generator = request.user
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your comment was submitted!'
                )
            return HttpResponseRedirect(reverse('play_display', args=[slug]))

        else:
            messages.add_message(
                request,
                messages.WARNING,
                'Invalid submit, please fill out all the required fields!'
                )
            return HttpResponseRedirect(reverse('play_display', args=[slug]))

        return render(
            request,
            "play_display.html",
            {
                'post': post,
                'comments': comments,
                'commented': True,
                'comment_form': comment_form,
            },
        )


class EditPlay(UpdateView):
    '''
    View to let the user edit a play event
    '''
    model = Play
    template_name = "edit_play.html"
    fields = ['setup', 'location', 'description', 'date', 'time', ]


def delete_play(request, slug):
    '''
    View to let the user delete a play event
    '''
    post = get_object_or_404(Play, slug=slug)
    post.delete()
    return redirect(reverse('play_events'))


class EditPlayComment(UpdateView):
    '''
    View to let the user edit a play event comment
    '''
    model = PlayComments
    template_name = 'edit_play_comment.html'
    form_class = PlayCommentsForm


def delete_play_comment(request, comments_id):
    '''
    View to let the user delete a play event
    '''
    comments = get_object_or_404(PlayComments, id=comments_id)
    comments.delete()
    return HttpResponseRedirect(reverse(
        'play_display', args=[comments.post.slug]))


class UserPosts(View):
    '''
    View to render the users own posts
    '''
    def get(self, request):
        if request.user.is_authenticated:
            posts = Post.objects.filter(generator=request.user)
            plays = Play.objects.filter(generator=request.user)
            topics = Topic.objects.all()

            return render(
                request,
                'user_posts.html',
                {
                    "topic_list": topics,
                    "posts": posts,
                    "plays": plays
                }
            )

