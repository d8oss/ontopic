# Generated by Django 3.2.3 on 2021-05-31 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20210531_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='threads',
            name='user',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Создатель темы'),
        ),
    ]