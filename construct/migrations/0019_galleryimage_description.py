# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0018_auto_20161110_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='description',
            field=models.TextField(default=b'', max_length=100),
        ),
    ]
