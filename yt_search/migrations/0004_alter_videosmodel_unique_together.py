# Generated by Django 4.0.5 on 2022-09-11 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yt_search', '0003_alter_videosmodel_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='videosmodel',
            unique_together=set(),
        ),
    ]