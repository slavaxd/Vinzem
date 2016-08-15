# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0003_auto_20160812_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='tags',
        ),
    ]
