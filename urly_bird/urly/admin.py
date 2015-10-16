from django.contrib import admin
from models import Click, Accessed

# Register your models here.
class ClickAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'short', 'orig', 'timestamp']


# class AccessedAdmin(modelAdmin):
#     list_display = ['click', 'reader', 'accessed_timestamp']


admin.site.register(Click, ClickAdmin)
admin.site.register(Accessed, AccessedAdmin)
