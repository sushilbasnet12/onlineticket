from django.contrib import admin

# Register your models here.

from . import models


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumbnail_preview')

    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True


class MatchAdmin(admin.ModelAdmin):
    list_display = ('name', "game", "team1_name", "team1image_preview",
                    "team2_name", "team2image_preview", "start_time")
    readonly_fields = ('team1image_preview', "team2image_preview")

    def team1image_preview(self, obj):
        return obj.team1image_preview

    def team2image_preview(self, obj):
        return obj.team2image_preview


admin.site.register(models.Game, GameAdmin)

admin.site.register(models.Match, MatchAdmin)
