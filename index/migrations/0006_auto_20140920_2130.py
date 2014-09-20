# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_auto_20140808_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torrent',
            name='size',
            field=models.BigIntegerField(),
        ),
    ]
