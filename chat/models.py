from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.utils import timezone
from mainweb.models import CustomUser 


class ChatRoom(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1) # You can set a default user here
    name = models.CharField(max_length=255, default="New Chat Room")
    description = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)  # Set default value
    slug = models.SlugField(unique=True, blank=True, default="new-chat-room")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name





class ChatMessage(models.Model):
    room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    send_time = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.send_time}'
