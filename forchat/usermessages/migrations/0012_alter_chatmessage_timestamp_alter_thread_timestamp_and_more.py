# Generated by Django 4.2.4 on 2023-11-04 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermessages', '0011_alter_chatmessage_timestamp_alter_thread_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 23, 59, 41, 494108), editable=False),
        ),
        migrations.AlterField(
            model_name='thread',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 23, 59, 41, 493108), editable=False),
        ),
        migrations.AlterField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 23, 59, 41, 493108)),
        ),
    ]
