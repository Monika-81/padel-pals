from django import forms
from .models import Comments, Post, Contact, Play


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


class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = ('setup', 'location', 'description', 'date', 'time',)

        labels = {
            'setup': 'Searching for team or player'
        }

        widgets = {
            'location': forms.Textarea(attrs={
                'rows': 1,
                'placeholder': 'Enter location'
            }),

            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add description'
            }),

            'date': forms.DateTimeInput(attrs={
                'placeholder': 'Date for game',
                'type': 'date'
                },
                format=('%Y-%m-%d')
            ),
            'time': forms.DateTimeInput(attrs={
                'type': 'time'
                },
                format=('%H:%M:%S')
            ),
        }
