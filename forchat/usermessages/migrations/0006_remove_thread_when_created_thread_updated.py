# Generated by Django 4.2.4 on 2023-11-04 16:54

import datetime
import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermessages', '0005_remove_thread_updated_thread_when_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thread',
            name='When Created',
        ),
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 22, 24, 31, 729108), verbose_name=django.contrib.auth.models.User),
        ),
    ]
