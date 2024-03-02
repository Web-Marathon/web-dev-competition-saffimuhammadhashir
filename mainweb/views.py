from django.shortcuts import render,redirect
from allauth.account.forms import LoginForm, SignupForm
from allauth.account.views import SignupView
from .forms import CustomSignupForm
from .models import CustomUser
from .forms import BioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse


def edit_bio(request):
    if request.method == 'POST':
        form = BioForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data['bio']
            request.user.bio = bio
            request.user.check_bio = True  # Set check_bio to True
            request.user.save()
            return redirect('home')  # Redirect to user's profile or any other desired page
    else:
        form = BioForm(instance=request.user)  # Pre-populate the form with existing bio data if available
    return render(request, 'edit_bio.html', {'form': form})



class CustomSignupView(SignupView):
    form_class = CustomSignupForm

    def form_valid(self, form):
        # Save the user first
        user = form.save(self.request)
        
        # Get the bio field value from the form
        bio = form.cleaned_data.get('bio')
        
        # Set the bio field for the user
        if bio:
            user.bio = bio
            user.save()
        
        return super().form_valid(form)
    
# Create your views here.
def mainpage1(request):
    if request.user.is_authenticated and not request.user.check_bio:
        return redirect(reverse('edit_bio'))  # Redirect to edit_bio page
    
    current_user = request.user
    context = {
        'user': current_user,
    }

    return render(request, "main.html", context)