# Generated by Django 3.2.25 on 2024-05-27 20:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_rename_bookmark_book_bookmarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookmarks',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmarks', to=settings.AUTH_USER_MODEL),
        ),
    ]
