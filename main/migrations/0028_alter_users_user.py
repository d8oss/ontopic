# Generated by Django 3.2.3 on 2021-05-31 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user',
            field=models.CharField(max_length=900, verbose_name='Ник'),
        ),
    ]
