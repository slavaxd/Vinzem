# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0017_auto_20161110_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='galleryimage',
            name='event_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u043e\u0434\u0456\u0457', blank=True),
        ),
    ]
