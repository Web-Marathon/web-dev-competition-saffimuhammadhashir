# forms.py

from django import forms
from .models import ForumPost, ForumComment

class ForumPostForm(forms.ModelForm):
    class Meta:
        model = ForumPost
        fields = ['title', 'text']
        labels = {
            'title': 'Title',
            'text': 'Your Post',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 5}),
        }

class ForumCommentForm(forms.ModelForm):
    class Meta:
        model = ForumComment
        fields = ['text']
        labels = {
            'text': 'Your Comment',
        }
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3}),
        }
