# Generated by Django 3.2.3 on 2021-05-27 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_forums_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='threads',
            options={'ordering': ['-date'], 'verbose_name': 'Тема', 'verbose_name_plural': 'Темы'},
        ),
    ]
