# views.py

from django.shortcuts import render
from .models import ResourcePost
from django.http import JsonResponse

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

# views.py

def search_resources(request):
    query = request.GET.get('query')
    if query:
        # Perform a case-insensitive search for resource posts with titles containing the query
        search_results = ResourcePost.objects.filter(title__icontains=query)
        context = {'search_results': search_results}
        return render(request, 'resources/search_results.html', context)
    else:
        return render(request, 'resources/search_results.html', {'search_results': []})


def create_resource_post(request):
    if request.method == 'POST':
        form = ResourcePostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            if ResourcePost.objects.filter(title=title).exists():
                # Redirect back with an error message
                return render(request, 'resources/create_resource_post.html', {'form': form, 'error_message': 'A post with this title already exists.'})
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('resource_post_detail', slug=post.slug)
        else:
            # If the form is invalid, return the form data to the template
            return render(request, 'resources/create_resource_post.html', {'form': form})
    else:
        form = ResourcePostForm()
    return render(request, 'resources/create_resource_post.html', {'form': form})


def edit_resource_post(request, slug):
    post = get_object_or_404(ResourcePost, slug=slug)

    if request.method == 'POST':
        form = ResourcePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('resource_post_detail', slug=post.slug)
    else:
        form = ResourcePostForm(instance=post)

    return render(request, 'resources/edit_resource_post.html', {'form': form})
