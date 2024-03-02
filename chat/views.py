from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import ChatRoom, ChatMessage
from .forms import ChatRoomForm, ChatMessageForm
from django.utils.text import slugify
from django.http import JsonResponse

@login_required
def create_chat_room(request):
    if request.method == 'POST':
        form = ChatRoomForm(request.POST)
        if form.is_valid():
            chat_room = form.save(commit=False)
            chat_room.user = request.user
            chat_room.slug = slugify(chat_room.name)  # Set the slug automatically
            chat_room.save()
            return redirect('chat_room', slug=chat_room.slug)
    else:
        default_data = {'name': 'New Chat Room', 'description': 'This is a new chat room.'}
        form = ChatRoomForm(initial=default_data)
    return render(request, 'chat/create_chat_room.html', {'form': form})

@login_required
def chat_room(request, slug):
    chat_room = get_object_or_404(ChatRoom, slug=slug)
    chat_messages = chat_room.messages.all().order_by('send_time')  # Order by descending send_time

    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.user = request.user
            chat_message.room = chat_room
            chat_message.save()
            return redirect('chat_room', slug=slug)
    else:
        form = ChatMessageForm()

    return render(request, 'chat/chat_room.html', {
        'chat_room': chat_room,
        'chat_messages': chat_messages,
        'form': form
    })

@login_required
def check_new_messages(request, slug):
    chat_room = get_object_or_404(ChatRoom, slug=slug)
    chat_messages = chat_room.messages.filter(id__gt=request.GET.get('latest_message_id', 0)).order_by('send_time')
    new_messages = [{'user': message.user.username, 'content': message.content, 'send_time': message.send_time.strftime('%Y-%m-%d %H:%M:%S')} for message in chat_messages]
    return JsonResponse({'new_messages': new_messages})

@login_required
def send_message(request, slug):
    chat_room = get_object_or_404(ChatRoom, slug=slug)
    if request.method == 'POST':
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.user = request.user
            chat_message.room = chat_room
            chat_message.save()
            return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'})
