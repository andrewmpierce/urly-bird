from django.contrib import admin


from .models import Click, Stats


class ClickAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'timestamp', 'orig', 'short']

class StatsAdmin(admin.ModelAdmin):
    list_display = ['click', 'reader', 'timestamp']

admin.site.register(Click, ClickAdmin)
admin.site.register(Stats, StatsAdmin)
