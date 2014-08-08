# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20140808_0620'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TorrentStats',
            new_name='TorrentStat',
        ),
        migrations.RenameModel(
            old_name='Trackers',
            new_name='Tracker',
        ),
    ]
