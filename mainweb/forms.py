# forms.py
from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser 

class CustomSignupForm(SignupForm):
    bio = forms.CharField(max_length=500, required=False)
    
    
class BioForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 50}),  # Adjust rows and cols as needed
        }