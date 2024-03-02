# events/models.py

from django.db import models
from mainweb.models import CustomUser 
from django.utils.text import slugify

class CalendarEvent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    event_date = models.DateTimeField()
    name = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class RSVP(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(CalendarEvent, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} RSVP'd to {self.event.name}"
