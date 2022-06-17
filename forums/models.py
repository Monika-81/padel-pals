from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Topic(models.Model):
    '''
    model for forum topics
    '''
    topic = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.topic


class Post(models.Model):
    '''
    model for forum posts
    '''
    topic = models.ForeignKey(
        Topic, on_delete=models.CASCADE, related_name="topic_posts")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    generator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    likes = models.ManyToManyField(
        User, related_name="forum_likes", blank=True)

    class Meta:
        '''
        Sorts the comments in descending order
        '''
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        '''
        Returns number of likes
        '''
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_display', args=[self.slug])


class Comments(models.Model):
    '''
    model for forum comments
    '''
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    generator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_post_comments")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        '''
        Sorts the comments in descending order
        '''
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.content} by {self.generator}"

    def get_absolute_url(self):
        return reverse('post_display', args=[self.post.slug])


class Contact(models.Model):
    '''
    model for admin contact through contact form
    '''
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.first_name} {self.last_name}'


class Play(models.Model):
    '''
    model for finding  a player or a team setup
    '''
    SETUP_CHOICES = [
        ('Searching for a Player', 'Player'),
        ('Searching for a Team', 'Team'),
    ]

    generator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="play_posts")
    setup = models.CharField(max_length=100, choices=SETUP_CHOICES)
    location = models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    date = models.DateField()
    time = models.TimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.setup

    def get_absolute_url(self):
        return reverse('play_display', args=[self.slug])


class PlayComments(models.Model):
    '''
    model for play list comments
    '''
    post = models.ForeignKey(
        Play, on_delete=models.CASCADE, related_name="play_list_comments")
    generator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_play_comments")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.content} by {self.generator}"

    def get_absolute_url(self):
        return reverse('play_display', args=[self.post.slug])
