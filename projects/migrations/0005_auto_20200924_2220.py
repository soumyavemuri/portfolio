# Generated by Django 3.1.1 on 2020-09-24 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20200924_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='dateofProject',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
