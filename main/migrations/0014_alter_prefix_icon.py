# Generated by Django 3.2.3 on 2021-05-30 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_prefix_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefix',
            name='icon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.icon', verbose_name='Иконка'),
        ),
    ]
