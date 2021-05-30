from django.db import models
from django.contrib.auth.models import AbstractUser


# таблица с темами на форуме
class Threads(models.Model):
    # |---------------------------------------------------------------------------|
    # | auto_now_add=True - автоматически записывать в базу данных                |
    # | db_index=True - добавить индекс для сортировки                            |
    # | максимальная длина - max_length                                           |
    # | null=True, blank=True - сделать необязательное поле для заполнения        |
    # | verbose_name='Заголовок объявления' - экранное имя для упрощённого чтения |
    # |---------------------------------------------------------------------------|

    title = models.CharField(max_length=50, verbose_name='Заголовок')
    date = models.DateTimeField(auto_now_add=True, db_index=True)

    forum = models.ForeignKey('Forums', null=True, on_delete=models.PROTECT, verbose_name='Раздел')
    prefix = models.ForeignKey('Prefix', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Префикс')

    class Meta:
        verbose_name_plural = 'Темы'
        verbose_name = 'Тема'
        ordering = ['-date']


# таблица со списком разделов

class Forums(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    icon = models.ForeignKey('Icon', null=True, on_delete=models.PROTECT, verbose_name='Иконка')
    desc = models.CharField(max_length=100, verbose_name='Описание', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Разделы'
        verbose_name = 'Раздел'
        ordering = ['name']


# таблица с префиксами для форума

class Prefix(models.Model):
    name = models.CharField(max_length=50, verbose_name='Содержание префикса')
    color = models.CharField(max_length=100, verbose_name='Bootstrap цвет')
    icon = models.ForeignKey('Icon', null=True, blank=True, on_delete=models.PROTECT, verbose_name='Иконка')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Префиксы'
        verbose_name = 'Префикс'
        ordering = ['name']


# таблица с иконками

class Icon(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название иконки')
    svg = models.CharField(max_length=500, verbose_name='svg код иконки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Иконки'
        verbose_name = 'Иконка'
        ordering = ['name']


# таблица с постами

class Post(models.Model):
    date = models.DateTimeField(verbose_name='Время поста', auto_now_add=True)
    content = models.TextField(verbose_name='Содержание поста')
    thid = models.IntegerField(verbose_name='Id темы', null=True)
    like = models.IntegerField(verbose_name='Лайки', null=True)

    class Meta:
        verbose_name_plural = 'Посты'
        verbose_name = 'Пост'
        ordering = ['date']
