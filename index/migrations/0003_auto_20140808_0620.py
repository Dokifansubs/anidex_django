# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20140808_0620'),
    ]

    operations = [
        migrations.CreateModel(
            name='TorrentFile',
            fields=[
                ('torrent', models.OneToOneField(primary_key=True, serialize=False, to='index.Torrent')),
                ('name', models.CharField(max_length=200)),
                ('data', models.BinaryField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TorrentStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('info_hash', models.CharField(max_length=20)),
                ('query_date', models.DateTimeField(default=datetime.datetime.utcnow, blank=True)),
                ('seeders', models.IntegerField(default=0, blank=True)),
                ('leechers', models.IntegerField(default=0, blank=True)),
                ('completed', models.IntegerField(default=0, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trackers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='torrent',
            name='trackers',
            field=models.ManyToManyField(to=b'index.Trackers'),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='torrent',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='torrent',
            name='leechers',
        ),
        migrations.RemoveField(
            model_name='torrent',
            name='seeders',
        ),
        migrations.AlterField(
            model_name='torrent',
            name='groups',
            field=models.ManyToManyField(to=b'index.Group', blank=True),
        ),
        migrations.AlterField(
            model_name='torrent',
            name='likes',
            field=models.IntegerField(default=0, blank=True),
        ),
    ]
