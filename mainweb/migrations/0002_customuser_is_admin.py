# Generated by Django 4.2.10 on 2024-03-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainweb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
