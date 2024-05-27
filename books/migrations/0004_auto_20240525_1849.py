# Generated by Django 3.2.25 on 2024-05-25 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_auto_20240408_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookmark',
            field=models.ManyToManyField(blank=True, default=None, related_name='bookmark', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(max_length=1000),
        ),
    ]