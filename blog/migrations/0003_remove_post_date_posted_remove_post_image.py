# Generated by Django 5.0.6 on 2024-06-24 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]