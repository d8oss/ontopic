# Generated by Django 3.2.3 on 2021-05-31 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_threads_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='threads',
            name='key',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Уникальный идентификатор'),
        ),
    ]
