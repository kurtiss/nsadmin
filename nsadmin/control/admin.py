from django.contrib import admin
from . import models


class PlaylistItemInline(admin.TabularInline):
	model = models.PlaylistItem
	extra = 1

class PlaylistAdmin(admin.ModelAdmin):
	inlines = [PlaylistItemInline]

class PlaylistItemAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, dict(fields = ["playlist"])),
		('Media Information', dict(fields = ["media_uri", "media_runtime_millis", "media_start_millis", "media_end_millis", "media_playback_rate"])),
		("Video Information", dict(fields = ["video_track", "video_aspect_ratio"])),
		("Audio Information", dict(fields = ["audio_volume", "audio_track", "audio_delay_millis"])),
		("Subtitle Information", dict(fields = ["subtitle_uri", "subtitle_track", "subtitle_delay_millis"]))
	]

# Register your models here.
admin.site.register(models.Playlist, PlaylistAdmin)
admin.site.register(models.PlaylistItem, PlaylistItemAdmin)
admin.site.register(models.PlaylistSyncPoint)
admin.site.register(models.VeeziSyncPoint)
admin.site.register(models.ScheduleEntry)