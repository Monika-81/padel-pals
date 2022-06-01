from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Topic(models.Model):
    #  model for forum topics
    topic = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


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
        return self.name

    def number_of_likes(self):
        return self.likes.count()    


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