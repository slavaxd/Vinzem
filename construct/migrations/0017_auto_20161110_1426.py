# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0016_galleryimage_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbf\xd0\xbe\xd0\xb4\xd1\x96\xd1\x97'),
        ),
    ]
