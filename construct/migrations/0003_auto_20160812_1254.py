# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0002_sevice'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sevice',
            new_name='Service',
        ),
    ]
