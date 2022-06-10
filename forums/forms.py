from django import forms
from .models import Comments, Post, Contact, Play, PlayComments


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

        widgets = {
            'first_name': forms.Textarea(attrs={
                'placeholder': 'First Name',
                'rows': 1,
            }),
            'last_name': forms.Textarea(attrs={
                'placeholder': 'Last Name',
                'rows': 1,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email adress'
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Please tell us what we can help you with!'
            }),
        }


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


class PlayCommentsForm(forms.ModelForm):
    class Meta:
        model = PlayComments
        fields = ('content',)
