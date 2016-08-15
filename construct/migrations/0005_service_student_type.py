# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0004_remove_galleryimage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='student_type',
            field=models.CharField(default=0, max_length=1, choices=[(0, b'Low'), (1, b'Normal'), (2, b'High')]),
            preserve_default=False,
        ),
    ]
