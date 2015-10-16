from django.contrib import admin

# Register your models here.
class BirdAdmin(admin.ModelAdmin):
    pass


class ClickAdmin(admin.ModelAdmin):
    pass


class AccessedAdmin(modelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)
admin.site.register(Rater, RaterAdmin)
admin.site.register(Rating, RatingAdmin)
