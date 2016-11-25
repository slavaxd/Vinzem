# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0020_indexbehindlinkfield'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='IndexBehindLinkField',
            new_name='IndexBehindLink',
        ),
    ]
