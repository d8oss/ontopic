# Generated by Django 3.2.3 on 2021-05-27 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210527_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='thread',
        ),
    ]
