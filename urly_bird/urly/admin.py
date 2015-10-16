from django.contrib import admin
from .models import Click


class ClickAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'timestamp', 'orig', 'short']



admin.site.register(Click, ClickAdmin)
