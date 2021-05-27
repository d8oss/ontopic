from django.contrib import admin
from .models import Threads, Forums, Prefix, Icon, Post


# коректное отображение таблицы Threads
class ThAdmin(admin.ModelAdmin):
    list_display = ('title', 'forum', 'date', 'prefix', 'pk')  # порядок


class PoAdmin(admin.ModelAdmin):
    list_display = ('content', 'date', 'like', 'thid')  # порядок


# регистрация таблиц в админке сайта
admin.site.register(Threads, ThAdmin)
admin.site.register(Forums)
admin.site.register(Prefix)
admin.site.register(Icon)
admin.site.register(Post, PoAdmin)
# -----------------------------------
