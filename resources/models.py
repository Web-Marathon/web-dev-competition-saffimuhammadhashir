from django.db import models
from django.utils.text import slugify
from mainweb.models import CustomUser  # Import your custom user model

class ResourcePost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Use CustomUser model
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    body = models.TextField()  # Change to TextField
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
