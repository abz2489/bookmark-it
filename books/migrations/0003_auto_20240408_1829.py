# Generated by Django 3.2.25 on 2024-04-08 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_book_isbn'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='cover_url',
        ),
        migrations.AddField(
            model_name='book',
            name='date_published',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='number_in_series',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='series',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
