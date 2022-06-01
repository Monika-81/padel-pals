from django.contrib import admin
from .models import Post, Topic
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'description')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
