# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0010_auto_20160815_1617'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', populate_from=b'title', editable=False),
            preserve_default=False,
        ),
    ]
