# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0015_auto_20161025_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
    ]
