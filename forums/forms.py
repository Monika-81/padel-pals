from django import forms
from .models import Comments, Post


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'title', 'content',)
