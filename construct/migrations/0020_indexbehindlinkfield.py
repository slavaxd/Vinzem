# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('construct', '0019_galleryimage_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexBehindLinkField',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', ckeditor.fields.RichTextField(max_length=100000)),
            ],
            options={
                'verbose_name': '\u041f\u043e\u043b\u0435 \u0432\u043d\u0438\u0437\u0443 \u0437 HTML',
            },
        ),
    ]
