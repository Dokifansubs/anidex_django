# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20140808_0629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrent',
            name='info_hash',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='torrentstat',
            name='info_hash',
            field=models.CharField(max_length=40),
        ),
    ]
