from django.contrib import admin
from .models import Threads, Forums, Prefix, Icon, Post, Users


# коректное отображение таблицы Threads
class ThAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'date', 'prefix', 'pk', 'user')  # порядок


class PoAdmin(admin.ModelAdmin):
    list_display = ('date', 'like', 'thid', 'user')  # порядок


class FrAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'icon')


class UsAdmin(admin.ModelAdmin):
    list_display = ('user', 'like', 'date', 'pk', 'stat', 'telegram', 'vk', 'color')


# регистрация таблиц в админке сайта
admin.site.register(Threads, ThAdmin)
admin.site.register(Forums, FrAdmin)
admin.site.register(Prefix)
admin.site.register(Icon)
admin.site.register(Post, PoAdmin)
admin.site.register(Users, UsAdmin)
# -----------------------------------
