from django import forms
from .models import Comments, Post, Contact


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('topic', 'title', 'content',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'content',)
