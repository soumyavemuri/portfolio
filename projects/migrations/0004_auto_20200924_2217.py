# Generated by Django 3.1.1 on 2020-09-24 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20200924_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='dateofProject',
            field=models.DateField(default=datetime.datetime(2020, 9, 24, 16, 47, 43, 378192, tzinfo=utc)),
        ),
    ]
