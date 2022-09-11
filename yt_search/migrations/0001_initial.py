# Generated by Django 4.0.5 on 2022-09-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideosModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Video Title')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('published_on', models.DateTimeField(verbose_name='Publishing datetime')),
                ('thumbnails_urls', models.URLField(max_length=255, verbose_name='Thumbnail URLs')),
                ('video_link', models.URLField(max_length=255, verbose_name='Video Link')),
            ],
            options={
                'db_table': 'Videos Database',
                'ordering': ['-published_on'],
            },
        ),
    ]
