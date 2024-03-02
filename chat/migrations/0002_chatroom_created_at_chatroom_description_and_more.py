# Generated by Django 4.2.10 on 2024-03-02 13:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatroom',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='chatroom',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='name',
            field=models.CharField(default='New Chat Room', max_length=255),
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='slug',
            field=models.SlugField(blank=True, default='new-chat-room', unique=True),
        ),
    ]