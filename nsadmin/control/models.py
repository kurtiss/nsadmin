from django.db import models


class Playlist(models.Model):
	SORT_NORMAL = '0,0'
	SORT_NAME = '0,1'
	SORT_AUTHOR = '0,3'
	SORT_RANDOM = '0,5'
	SORT_TRACK = '0,7'
	SORT_REVERSE = '1,0'
	SORT_NAME_REVERSE = '1,1'
	SORT_AUTHOR_REVERSE = '1,3'
	SORT_TRACK_REVERSE = '1,7'
	SORT_ORDER_CHOICES = (
		(SORT_NORMAL, 'Normal'),
		(SORT_NAME, 'By Name'),
		(SORT_AUTHOR, 'By Author'),
		(SORT_RANDOM, 'Random'),
		(SORT_TRACK, 'By Track'),
		(SORT_REVERSE, 'Reverse Order'),
		(SORT_NAME_REVERSE, 'By Name (Reversed)'),
		(SORT_AUTHOR_REVERSE, 'By Author (Reversed)'),
		(SORT_TRACK_REVERSE, 'By Track (Reversed)')
	)

	name = models.CharField(max_length = 256)
	sort_order = models.CommaSeparatedIntegerField(max_length = 3, choices = SORT_ORDER_CHOICES, default = SORT_NORMAL)

	def __unicode__(self):
		return unicode(str(self))

	def __str__(self):
		return "PLAYLIST: <{0}>".format(self.name)


class PlaylistItem(models.Model):
	AR0 = ''
	AR1_1 = '1:1'
	AR4_3 = '4:3'
	AR5_4 = '5:4'
	AR16_9 = '16:9'
	AR16_10 = '16:10'
	AR221_100 = '221:100'
	AR235_100 = '235:100'
	AR239_100 = '239:100'

	ASPECT_RATIO_CHOICES = (
		(AR0, '(Default)'),
		(AR1_1, '1:1 (Square)'),
		(AR4_3, '4:3 (TV)'),
		(AR5_4, '5:4'),
		(AR16_9, '16:9 (Widescreen TV)'),
		(AR221_100, '221:100 (70mm)'),
		(AR235_100, '235:100 (Early \'Scope)'),
		(AR239_100, '239:100 (Moden \'Scope)')
	)

	playlist = models.ForeignKey(Playlist, related_name = 'items')

	media_uri = models.CharField(max_length = 512)
	media_runtime_millis = models.PositiveIntegerField()
	media_start_millis = models.PositiveIntegerField(default = 0)
	media_end_millis = models.IntegerField(default = -1)
	media_playback_rate = models.PositiveIntegerField(default = 1)

	video_track = models.PositiveSmallIntegerField(default = 0)
	video_aspect_ratio = models.CharField(max_length = 32, choices = ASPECT_RATIO_CHOICES, default = AR0)

	audio_track = models.PositiveSmallIntegerField(default = 0)
	audio_delay_millis = models.IntegerField(default = 0)
	audio_volume = models.PositiveSmallIntegerField(default = 100)

	subtitle_uri = models.CharField(max_length = 512)
	subtitle_track = models.PositiveSmallIntegerField(default = 0)
	subtitle_delay_millis = models.IntegerField(default = 0)


class PlaylistSyncPoint(models.Model):
	playlist = models.ForeignKey(Playlist)
	playlist_item = models.ForeignKey(PlaylistItem)
	offset_millis = models.IntegerField(default = 0)


class VeeziSyncPoint(models.Model):
	film_id = models.CharField(max_length = 16)
	offset_millis = models.IntegerField(default = 0)


class ScheduleEntry(models.Model):
	playlist_sync_point = models.ForeignKey(PlaylistSyncPoint)
	veezi_sync_point = models.ForeignKey(VeeziSyncPoint)