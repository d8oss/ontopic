from django.contrib import admin
from .models import Threads, Forums, Prefix, Icon


# коректное отображение таблицы Threads
class ThAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'forum', 'date', 'prefix')  # порядок


# регистрация таблиц в админке сайта
admin.site.register(Threads, ThAdmin)
admin.site.register(Forums)
admin.site.register(Prefix)
admin.site.register(Icon)
# -----------------------------------
