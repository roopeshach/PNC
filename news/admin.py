from django.contrib import admin
from .models import Event, News, Notice


# Register your models here.
class event(admin.ModelAdmin):
    list_display = ['title', 'date']


class news(admin.ModelAdmin):
    list_display = ['title', 'date']


class notice(admin.ModelAdmin):
    list_display = ['title', 'date']


admin.site.register(Event, event)
admin.site.register(News, news)
admin.site.register(Notice, notice)
