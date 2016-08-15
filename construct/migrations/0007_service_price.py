# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0006_auto_20160812_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
