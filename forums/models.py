from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField


class Topic(models.Model):
    #  model for forum topics
    topic = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.topic


class Post(models.Model):
    #  model for forum posts
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="topic_posts")
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    generator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name="forum_likes", blank=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_display', args=[self.slug])


class Comments(models.Model):
    #  model for forum comments
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    generator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_comments")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True) 
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name="comment_likes", blank=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return f"Comment {self.content} by {self.generator}"

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('post_display', args=[self.post.slug])


class Contact(models.Model):
    #  model for admin contact
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message {self.content} from {self.first_name} {self.last_name}'
