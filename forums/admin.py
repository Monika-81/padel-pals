from django.contrib import admin
from .models import Topic, Post, Comments, Contact, Play
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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name', 'email')
    list_display = ('first_name', 'last_name', 'email', 'created_date')
    search_fields = ['first_name', 'last_name', 'email', 'content']


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_filter = ('setup', 'date', 'time',)
    list_display = ('setup', 'location', 'date', 'time', 'generator')
