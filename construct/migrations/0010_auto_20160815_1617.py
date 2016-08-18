# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0009_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='datetime',
            field=models.TextField(),
        ),
    ]
