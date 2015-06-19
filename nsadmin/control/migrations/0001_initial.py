# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('sort_order', models.CommaSeparatedIntegerField(default=b'0,0', max_length=3, choices=[(b'0,0', b'Normal'), (b'0,1', b'By Name'), (b'0,3', b'By Author'), (b'0,5', b'Random'), (b'0,7', b'By Track'), (b'1,0', b'Reverse Order'), (b'1,1', b'By Name (Reversed)'), (b'1,3', b'By Author (Reversed)'), (b'1,7', b'By Track (Reversed)')])),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_uri', models.CharField(max_length=512)),
                ('media_runtime_millis', models.PositiveIntegerField()),
                ('media_start_millis', models.PositiveIntegerField(default=0)),
                ('media_end_millis', models.IntegerField(default=-1)),
                ('media_playback_rate', models.PositiveIntegerField(default=1)),
                ('video_track', models.PositiveSmallIntegerField(default=0)),
                ('video_aspect_ratio', models.CharField(default=b'', max_length=32, choices=[(b'', b'(Default)'), (b'1:1', b'1:1 (Square)'), (b'4:3', b'4:3 (TV)'), (b'5:4', b'5:4'), (b'16:9', b'16:9 (Widescreen TV)'), (b'221:100', b'221:100 (70mm)'), (b'235:100', b"235:100 (Early 'Scope)"), (b'239:100', b"239:100 (Moden 'Scope)")])),
                ('audio_track', models.PositiveSmallIntegerField(default=0)),
                ('audio_delay_millis', models.IntegerField(default=0)),
                ('audio_volume', models.PositiveSmallIntegerField(default=100)),
                ('subtitle_uri', models.CharField(max_length=512)),
                ('subtitle_track', models.PositiveSmallIntegerField(default=0)),
                ('subtitle_delay_millis', models.IntegerField(default=0)),
                ('playlist', models.ForeignKey(related_name='items', to='control.Playlist')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistSyncPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('offset_millis', models.IntegerField(default=0)),
                ('playlist', models.ForeignKey(to='control.Playlist')),
                ('playlist_item', models.ForeignKey(to='control.PlaylistItem')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('playlist_sync_point', models.ForeignKey(to='control.PlaylistSyncPoint')),
            ],
        ),
        migrations.CreateModel(
            name='VeeziSyncPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('film_id', models.CharField(max_length=16)),
                ('offset_millis', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='scheduleentry',
            name='veezi_sync_point',
            field=models.ForeignKey(to='control.VeeziSyncPoint'),
        ),
    ]
