# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='torrentfile',
            name='torrent',
        ),
        migrations.DeleteModel(
            name='TorrentFile',
        ),
        migrations.DeleteModel(
            name='TorrentStats',
        ),
        migrations.AddField(
            model_name='torrent',
            name='completed',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='torrent',
            name='leechers',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='torrent',
            name='seeders',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='torrent',
            name='trackers',
        ),
        migrations.DeleteModel(
            name='Trackers',
        ),
        migrations.AlterField(
            model_name='torrent',
            name='groups',
            field=models.ManyToManyField(to=b'index.Group'),
        ),
        migrations.AlterField(
            model_name='torrent',
            name='likes',
            field=models.IntegerField(),
        ),
    ]
