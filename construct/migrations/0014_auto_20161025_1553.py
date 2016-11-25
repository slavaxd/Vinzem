# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0013_auto_20160901_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
    ]
