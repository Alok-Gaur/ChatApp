# Generated by Django 4.2.4 on 2023-11-04 16:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermessages', '0007_alter_thread_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 4, 16, 58, 22, 786108, tzinfo=datetime.timezone.utc)),
        ),
    ]
