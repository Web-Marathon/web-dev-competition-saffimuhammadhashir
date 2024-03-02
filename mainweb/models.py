from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add your custom fields here
    bio = models.TextField(blank=True)
    check_bio = models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)