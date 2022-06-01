from django.contrib import admin
from .models import Post, Topic
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic', 'description')


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content')
    list_filter = ('created_date', 'topic__topic')
