from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import ForumPost, ForumComment
from django.urls import reverse
from .forms import ForumPostForm, ForumCommentForm

def create_forum_post(request):
    if request.method == 'POST':
        form = ForumPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  
            post.save()

            return redirect(reverse('forum_post_detail', kwargs={'slug': post.slug})) 
    else:
        form = ForumPostForm()
    return render(request, 'forum/create_forum_post.html', {'form': form})
from .forms import ForumCommentForm  # Import the form

def forum_post_detail(request, slug):
    post = get_object_or_404(ForumPost, slug=slug)
    comments = post.comments.all()
    comment_form = ForumCommentForm()  # Create an instance of the comment form

    return render(request, 'forum/forum_post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


def forum_page(request):
    posts = ForumPost.objects.all().order_by('-created_at')
    return render(request, 'forum/forum_page.html', {'posts': posts})

def get_comments(request, slug):
    post = ForumPost.objects.get(slug=slug)
    comments = post.comments.all().values('text', 'user__username','created_at')
    return JsonResponse(list(comments), safe=False)

def post_comment(request, slug):
    post = get_object_or_404(ForumPost, slug=slug)
    if request.method == 'POST':
        comment_form = ForumCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': comment_form.errors}, status=400)
