from django import forms
from .models import ResourcePost

class ResourcePostForm(forms.ModelForm):
    class Meta:
        model = ResourcePost
        fields = ['title', 'body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 5}),  # Customize the textarea appearance if needed
        }
