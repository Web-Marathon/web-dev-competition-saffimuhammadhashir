# views.py

from django.shortcuts import render
from .models import ResourcePost

def all_resource_posts(request):
    posts = ResourcePost.objects.all()
    return render(request, 'resources/all_resource_posts.html', {'posts': posts})


# views.py

from django.shortcuts import render, get_object_or_404
from .models import ResourcePost

def resource_post_detail(request, slug):
    post = get_object_or_404(ResourcePost, slug=slug)
    return render(request, 'resources/resource_post_detail.html', {'post': post})


# views.py

from django.shortcuts import render, redirect
from .forms import ResourcePostForm

def create_resource_post(request):
    if request.method == 'POST':
        form = ResourcePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('resources/resource_post_detail', slug=post.slug)
    else:
        form = ResourcePostForm()
    return render(request, 'resources/create_resource_post.html', {'form': form})
