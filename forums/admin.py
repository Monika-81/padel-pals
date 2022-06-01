from django.contrib import admin
from .models import Topic, Post, Comments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'description')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('created_date', 'topic__topic')
    list_display = ('title', 'topic', 'created_date', 'generator')
    search_fields = ['title', 'content', 'generator__username']


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_filter = ('created_date', 'generator')
    list_display = ('content', 'created_date', 'generator')
    search_fields = ['content', 'generator__username']
