# Generated by Django 3.2.3 on 2021-05-27 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_threads_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thread', models.IntegerField(verbose_name='id темы сообщения')),
                ('date', models.DateTimeField(verbose_name='Время поста')),
                ('content', models.TextField(verbose_name='Содержание поста')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['date'],
            },
        ),
    ]
