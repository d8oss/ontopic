# Generated by Django 3.2.3 on 2021-05-24 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210524_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prefix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Содержание префикса')),
                ('color', models.CharField(max_length=100, verbose_name='Bootstrap цвет')),
            ],
            options={
                'verbose_name': 'Префикс',
                'verbose_name_plural': 'Префиксы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='threads',
            name='prefix',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='main.prefix', verbose_name='Префикс'),
        ),
    ]